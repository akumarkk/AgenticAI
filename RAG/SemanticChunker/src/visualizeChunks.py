import csv
# from langchain_text_splitters import SemanticChunker
from langchain_experimental.text_splitter import SemanticChunker
from langchain_ollama import OllamaEmbeddings

# 1. Initialize local embedding model on custom port 11454
embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://127.0.0.1:11434"
)

# Sample Document
sample_text = """
Retrieval-Augmented Generation (RAG) optimizes LLM responses using external knowledge bases.
Traditional chunking methods split text based on character or token counts.
However, fixed-size chunking often cuts sentences in half or breaks semantic context.

Semantic chunking solves this by analyzing sentence embeddings.
It measures cosine distance between adjacent sentences and identifies topic shifts.
When the semantic distance exceeds a threshold, a new chunk boundary is created.

Machine learning models require clean, well-formatted training data.
Overfitting occurs when a model learns noise instead of actual patterns in data.
Regularization techniques like L1 and L2 help prevent overfitting during model training.

Neural networks consist of input, hidden, and output layers.
Backpropagation updates weights based on calculated loss values.
Gradient descent minimizes loss functions during optimization.
"""

# 2. Chunk text semantically
chunker = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=70.0
)

docs = chunker.create_documents([sample_text])
print(f"Generated {len(docs)} chunks.")

# 3. Compute vector embeddings for each generated chunk
chunk_texts = [doc.page_content.strip() for doc in docs]
vectors = embeddings.embed_documents(chunk_texts)

# 4. Export vectors.tsv (numerical embeddings)
with open("vectors.tsv", "w", encoding="utf-8", newline="") as f_vec:
    writer = csv.writer(f_vec, delimiter="\t")
    for vec in vectors:
        writer.writerow(vec)

# 5. Export metadata.tsv (Chunk ID and Content)
with open("metadata.tsv", "w", encoding="utf-8", newline="") as f_meta:
    writer = csv.writer(f_meta, delimiter="\t")
    # Header line for TensorBoard metadata
    writer.writerow(["Chunk_ID", "Text_Content"])
    for i, text in enumerate(chunk_texts):
        # Clean newlines to keep metadata aligned
        clean_text = text.replace("\n", " ")
        writer.writerow([f"Chunk_{i+1}", clean_text])

print(" Successfully created 'vectors.tsv' and 'metadata.tsv'!")