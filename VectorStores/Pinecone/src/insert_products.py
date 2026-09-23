import json
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

# Configuration Constants
INDEX_NAME = "electronics-catalog"
MODEL_NAME = "all-MiniLM-L6-v2"
DIMENSION = 384  # Matches all-MiniLM-L6-v2 output dimension


def initialize_pinecone():
  pc = Pinecone()  # Automatically picks up PINECONE_API_KEY environment variable
  if INDEX_NAME not in [i["name"] for i in pc.list_indexes()]:
    pc.create_index(
        name=INDEX_NAME,
        dimension=DIMENSION,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
  return pc.Index(INDEX_NAME)


def load_products(filepath="../data/products.json"):
  with open(filepath, "r", encoding="utf-8") as f:
    return json.load(f)


def main():
  print("Initializing Hugging Face embedding model...")
  hf_model = SentenceTransformer(MODEL_NAME)

  print("Connecting to Pinecone...")
  index = initialize_pinecone()

  print(f"Loading products from data source...")
  products = load_products("products.json")

  vectors_to_upsert = []
  for prod in products:
    # Generate local embedding vector from product description text
    embedding = hf_model.encode(prod["text"]).tolist()

    vectors_to_upsert.append({
        "id": prod["id"],
        "values": embedding,
        "metadata": prod["metadata"],
    })

  # Perform bulk upsert into Pinecone
  print(f"Upserting {len(vectors_to_upsert)} products into Pinecone...")
  index.upsert(vectors=vectors_to_upsert)
  print("Successfully completed product ingestion!")


if __name__ == "__main__":
  main()