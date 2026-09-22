import requests

response = requests.post(
    "http://127.0.0.1:8989/v1/embeddings",
    json={"input": ["Hello from Flowise!", "Running local embeddings"]}
)

print(response.json())