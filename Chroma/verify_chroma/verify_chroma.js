import { ChromaClient } from 'chromadb';

const client = new ChromaClient({
  path: "http://127.0.0.1:8000"
});

async function checkConnection() {
  try {
    // Send a heartbeat request to check if Chroma is reachable
    const pulse = await client.heartbeat();
    const version = await client.version();
    
    console.log(" Successfully connected to ChromaDB!");
    console.log(`Heartbeat timestamp: ${pulse}`);
    console.log(`ChromaDB Version: ${version}`);
  } catch (error) {
    console.error(" Failed to connect to ChromaDB:", error);
  }
}

checkConnection();