import chromadb

# Initialize the Chroma HTTP client using your ngrok URL
client = chromadb.HttpClient(
    host="pantyhose-user-botany.ngrok-free.dev",
    port=443,
    ssl=True
)

# 1. List all existing collections in your vector store
collections = client.list_collections()
print("Collections found:", [c.name for c in collections])

# 2. Select a specific collection (replace 'your_collection_name' with your actual collection)
collection_name = "returns_policy_ecomm"
collection = client.get_collection(name=collection_name)

# 3. Query the collection (Chroma will automatically embed the query text if using a default embedding function, or pass query_embeddings directly)
results = collection.query(
    query_texts=["Your search query here"],
    n_results=3
)

# 4. Print the results
print("Query Results:")
print(results)