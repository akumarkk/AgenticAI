from sentence_transformers import SentenceTransformer
from pinecone_text.sparse import BM25Encoder


class HybridEncoder:
    """Handles generation of dense (semantic) and sparse (keyword) vectors."""
    
    def __init__(self, dense_model_name: str = "all-MiniLM-L6-v2"):
        self.dense_model = SentenceTransformer(dense_model_name)
        # Uses pre-fitted MS MARCO params for immediate default usage
        self.sparse_encoder = BM25Encoder.default()

    def encode_text(self, text: str) -> tuple[list[float], dict]:
        """Generates both dense and sparse embeddings for a single text payload."""
        dense_vec = self.dense_model.encode(text).tolist()
        sparse_vec = self.sparse_encoder.encode_documents(text)
        return dense_vec, sparse_vec

    def encode_query(self, query: str) -> tuple[list[float], dict]:
        """Generates raw dense and sparse embeddings for a query."""
        dense_vec = self.dense_model.encode(query).tolist()
        sparse_vec = self.sparse_encoder.encode_queries(query)
        return dense_vec, sparse_vec