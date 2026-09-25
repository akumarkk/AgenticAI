import os
from pinecone import Pinecone, ServerlessSpec


class PineconeVectorStore:
    """Manages Pinecone index lifecycle and record upserts."""
    
    def __init__(self, index_name: str, dimension: int = 384, api_key: str | None = None):
        # 1. Option A (Recommended): Pass api_key directly if provided, 
        # otherwise let Pinecone automatically read PINECONE_API_KEY from environment.
        self.pc = Pinecone(api_key=api_key) if api_key else Pinecone()
        
        self.index_name = index_name
        self.dimension = dimension
        
        self._ensure_index_exists()
        self.index = self.pc.Index(self.index_name)

    def _ensure_index_exists(self):
        existing_indexes = [idx.name for idx in self.pc.list_indexes()]
        if self.index_name not in existing_indexes:
            self.pc.create_index(
                name=self.index_name,
                dimension=self.dimension,
                metric="dotproduct",
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )

    def batch_upsert(self, records: list[dict]):
        """Upserts a list of formatted vector dictionary objects."""
        self.index.upsert(vectors=records)