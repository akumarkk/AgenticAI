import os
import sys
import cohere

# Initialize Cohere Client
api_key = os.environ.get("COHERE_API_KEY")
if not api_key:
    raise ValueError("COHERE_API_KEY environment variable is not set.")

co = cohere.ClientV2(api_key=api_key)

DOCS_FILE = "../data/documents.txt"

def load_documents(filepath):
    if not os.path.exists(filepath):
        print(f"Error: Document file '{filepath}' not found.")
        sys.exit(1)
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

documents = load_documents(DOCS_FILE)

print(f"Loaded {len(documents)} documents.")
print("Type a query to test documents rerank. Type 'q' to quit.\n")

while True:
    try:
        user_query = input("\nEnter search query: ").strip()
        if user_query.lower() in ["q", "quit", "exit"]:
            break
        if not user_query:
            continue

        # Ask for top N results to evaluate score drop-off
        top_n_input = input("How many top docs to return? (default 5): ").strip()
        top_n = int(top_n_input) if top_n_input.isdigit() else 5

        response = co.rerank(
            model="rerank-v3.5",
            query=user_query,
            documents=documents,
            top_n=top_n
        )

        print(f"\nQuery: '{user_query}'")
        print("=" * 65)
        print(f"{'Rank':<6}{'Original Index':<16}{'Score':<10}{'Document Excerpt'}")
        print("-" * 65)

        for rank, hit in enumerate(response.results, start=1):
            original_idx = hit.index
            score = hit.relevance_score
            excerpt = documents[original_idx]
            print(f"#{rank:<5} Index {original_idx:<10} {score:.4f}    {excerpt}")

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Error: {e}")