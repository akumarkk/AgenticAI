import cohere
import os

# Replace with your actual Cohere API key
# Retrieve the key from the environment
api_key = os.environ.get("COHERE_API_KEY")

if not api_key:
    raise ValueError("Cohere API key not found...")

try:
    # Initialize the v2 client
    co = cohere.ClientV2(api_key)
    
    # Send a lightweight request to verify connection
    response = co.rerank(
        model="rerank-v3.5",
        query="test query",
        documents=["test document"],
        top_n=1
    )
    
    print("Connection successful! Cohere API is reachable.")
    print("Test Response:", response)

except cohere.core.api_error.ApiError as e:
    print(f"API Error (Check your API key or permissions): {e}")
except Exception as e:
    print(f"Failed to connect to Cohere: {e}")