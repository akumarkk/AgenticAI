from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

pc = Pinecone()
index = pc.Index("electronics-catalog")
hf_model = SentenceTransformer("all-MiniLM-L6-v2")

# User search query
query_text = "comfortable headphones for music"
query_vector = hf_model.encode(query_text).tolist()

# Query with metadata filter (e.g., Audio category AND currently InStock)
results = index.query(
    vector=query_vector,
    top_k=2,
    include_metadata=True,
    filter={"$and": [{"Category": {"$eq": "Audio"}}, {"InStock": {"$eq": True}}]},
)

print("\n--- Filtered Product Results ---")
for match in results["matches"]:
  print(f"ID: {match['id']} | Score: {match['score']:.4f}")
  print(f"Metadata: {match['metadata']}")
  print("-" * 30)