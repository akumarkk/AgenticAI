class HybridSearchEngine:
    """Executes hybrid queries across the vector store with tunable alpha parameters."""
    
    def __init__(self, encoder, vector_store):
        self.encoder = encoder
        self.vector_store = vector_store

    def search(self, query: str, alpha: float = 0.5, top_k: int = 3) -> list[dict]:
        """
        Executes a weighted hybrid search query.
        alpha = 1.0 -> Pure Dense (Semantic)
        alpha = 0.0 -> Pure Sparse (Keyword)
        alpha = 0.5 -> Equal Balance
        """
        raw_dense, raw_sparse = self.encoder.encode_query(query)

        # Scale vectors based on the alpha weight
        scaled_dense = [val * alpha for val in raw_dense]
        scaled_sparse = {
            "indices": raw_sparse["indices"],
            "values": [val * (1.0 - alpha) for val in raw_sparse["values"]]
        }

        response = self.vector_store.index.query(
            vector=scaled_dense,
            sparse_vector=scaled_sparse,
            top_k=top_k,
            include_metadata=True
        )

        return [
            {
                "id": match["id"],
                "score": round(match["score"], 4),
                "metadata": match["metadata"]
            }
            for match in response["matches"]
        ]