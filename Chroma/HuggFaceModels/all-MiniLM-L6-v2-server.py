from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import uvicorn

app = FastAPI()

# Load model locally into memory
print("Loading model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
print("Model loaded successfully!")

class EmbeddingRequest(BaseModel):
    input: list[str]

@app.post("/v1/embeddings")
async def get_embeddings(request: EmbeddingRequest):
    try:
        # Generate embeddings
        embeddings = model.encode(request.input).tolist()
        
        # Format matching OpenAI-style response structure often used by local connectors
        data = [
            {"object": "embedding", "index": i, "embedding": emb}
            for i, emb in enumerate(embeddings)
        ]
        return {"object": "list", "data": data, "model": "all-MiniLM-L6-v2"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8989)