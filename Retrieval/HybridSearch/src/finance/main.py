import csv

from flask import json
from encoders import HybridEncoder
from vector_store import PineconeVectorStore
from search_engine import HybridSearchEngine


def load_datasetcsv(file_path: str) -> list[dict]:
    """Helper to read CSV documents."""
    with open(file_path, mode="r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def load_dataset(file_path: str) -> list[dict]:
    """Loads a standard JSON file containing a list of dictionaries."""
    with open(file_path, mode="r", encoding="utf-8") as f:
        return json.load(f)


def main():
    INDEX_NAME = "financestatements-modular-hybrid-demo"
    DATASET_PATH = "../../data/finance/financial_statements_2026.csv"

    # 1. Initialize Components
    encoder = HybridEncoder()
    store = PineconeVectorStore(index_name=INDEX_NAME)
    search_engine = HybridSearchEngine(encoder=encoder, vector_store=store)

    # 2. Ingest Data
    raw_docs = load_dataset(DATASET_PATH)
    vectors_to_upsert = []

    for doc in raw_docs:
        full_text = f"{doc['merchant_code']} - {doc['description']} ({doc['category']})"
        dense_emb, sparse_emb = encoder.encode_text(full_text)

        vectors_to_upsert.append({
            "id": doc["id"],
            "values": dense_emb,
            "sparse_values": sparse_emb,
            "metadata": {
                "merchant_code": doc["merchant_code"],
                "amount": float(doc["amount"]),
                "category": doc["category"],
                "text": full_text
            }
        })

    store.batch_upsert(vectors_to_upsert)
    print(f"Indexed {len(vectors_to_upsert)} items into '{INDEX_NAME}'.\n")

    # 3. Query Execution Example
    query = "subscription charges for netflix $15.49"
    results = search_engine.search(query=query, alpha=0.5, top_k=3)

    print(f"Results for query: '{query}'")
    for rank, res in enumerate(results, start=1):
        print(f"[{rank}] Score: {res['score']} | ID: {res['id']}")
        print(f"    Text: {res['metadata']['text']}\n")


if __name__ == "__main__":
    main()