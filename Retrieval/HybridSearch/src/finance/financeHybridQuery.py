import os
from pathlib import Path
from pinecone import Pinecone, ServerlessSpec
from pinecone_text.sparse import BM25Encoder
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader


# -------------------------------------------------------------------
# 1. Document Reader Helper Functions
# -------------------------------------------------------------------
def load_text_from_file(file_path: str) -> str:
    """Reads raw text from .txt, .md, or .pdf files."""
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
        
    if path.suffix.lower() in [".txt", ".md"]:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
            
    elif path.suffix.lower() == ".pdf":
        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        return text
    else:
        raise ValueError(f"Unsupported file format: {path.suffix}")


# -------------------------------------------------------------------
# 2. Main File Ingestion Pipeline
# -------------------------------------------------------------------
def ingest_file_to_pinecone(file_path: str, index_name: str = "hybrid-docs-demo"):
    # Initialize Pinecone
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY", "your-api-key-here"))
    
    # Ensure Index exists
    if index_name not in [idx.name for idx in pc.list_indexes()]:
        pc.create_index(
            name=index_name,
            dimension=384,  # Matching 'all-MiniLM-L6-v2'
            metric="dotproduct",  # Mandatory metric for Pinecone Sparse-Dense
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
    index = pc.Index(index_name)

    # Models Initialization
    dense_model = SentenceTransformer("all-MiniLM-L6-v2")
    bm25 = BM25Encoder.default()  # Pre-fitted on MS MARCO for fast evaluation

    # Step A: Load text from file
    print(f"Loading content from: {file_path}")
    raw_text = load_text_from_file(file_path)

    # Step B: Chunk document into smaller fragments
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50,
        length_function=len
    )
    chunks = splitter.split_text(raw_text)
    print(f"Split document into {len(chunks)} chunks.")

    # Step C: Prepare vectors and batch upsert
    vectors_to_upsert = []
    file_name = Path(file_path).name

    for idx, chunk in enumerate(chunks):
        chunk_id = f"{file_name}_chunk_{idx}"
        
        # Dense & Sparse embeddings
        dense_emb = dense_model.encode(chunk).tolist()
        sparse_emb = bm25.encode_documents(chunk)

        vectors_to_upsert.append({
            "id": chunk_id,
            "values": dense_emb,
            "sparse_values": sparse_emb,
            "metadata": {
                "source_file": file_name,
                "chunk_index": idx,
                "text": chunk
            }
        })

    # Batch upsert to Pinecone
    index.upsert(vectors=vectors_to_upsert)
    print(f"Successfully upserted {len(vectors_to_upsert)} chunks to Pinecone!")


# -------------------------------------------------------------------
# 3. Execution Example
# -------------------------------------------------------------------
if __name__ == "__main__":
    # Point this to your target text or PDF file
    SAMPLE_FILE = "sample_financial_report.txt"
    
    # Create a quick dummy file if one doesn't exist
    if not os.path.exists(SAMPLE_FILE):
        with open(SAMPLE_FILE, "w", encoding="utf-8") as f:
            f.write(
                "Q3 Financial Report - Enterprise Accounts:\n"
                "In July 2026, recurring subscription charges for Netflix were processed under ID TST* NETFLIX.COM.\n"
                "Total operational expenditure increased by 12% across cloud services including AWS and GCP.\n"
                "Invoice ID #INV-99201 was settled for vendor Chevron Gas."
            )

    ingest_file_to_pinecone(file_path=SAMPLE_FILE)