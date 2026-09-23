import chromadb
from chromadb.utils import embedding_functions

# 1. Initialize the Chroma client (Persistent or Ephemeral)
#client = chromadb.PersistentClient(path="./chroma_db")
client = chromadb.HttpClient(host="localhost", port=8676)

# 2. Set up the embedding function explicitly (optional, as all-MiniLM-L6-v2 is the default)
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# 3. Get or create the collection with the embedding function
collection = client.get_or_create_collection(
    name="returns_policy_ecommv2",
    embedding_function=embedding_fn
)

# 4. Upsert your data
# Upsert will insert new records or update existing ones based on the matching IDs.
collection.upsert(
    ids=["Doc1", "Doc2", "Doc3"],
    documents=[
        "Chroma is an open-source vector database.",
        "Sentence transformers make it easy to generate embeddings locally.",
        "Upsert operations either insert new data or update existing records."
    ],
    metadatas=[
        {"Source": "Documentation", "Version": "1.0"},
        {"Source": "Guide", "Version": "2.0"},
        {"Source": "Tutorial", "Version": "1.1"}
    ]
)

print(f"Successfully upserted data. Total count: {collection.count()}")