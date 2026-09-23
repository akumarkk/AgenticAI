import chromadb

# Connect to your local ChromaDB instance
client = chromadb.HttpClient(host="127.0.0.1", port=8000)

# Get or create the collection matching your Flowise setup
collection = client.get_or_create_collection(name="returns_policy_ecomm")

# Add documents, unique IDs, and metadata
collection.add(
    documents=[
        "Amazon Return Policy: Items can be returned within 30 days of receipt.",
        "Walmart Return Policy: Most items can be returned within 90 days."
    ],
    metadatas=[
        {"source": "amazon_returns_policy.txt"},
        {"source": "walmart_returns_policy.txt"}
    ],
    ids=["doc1", "doc2"]
)

print("Documents added successfully!")