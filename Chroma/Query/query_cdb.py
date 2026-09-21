import chromadb

# Initialize Chroma and collection
ClientInstance = chromadb.HttpClient(
    host="pantyhose-user-botany.ngrok-free.dev",
    port=443,
    ssl=True
)

# ClientInstance = chromadb.Client()
CollectionInstance = ClientInstance.get_collection(name="returns_policy_ecomm")

CurrentBuffer = []
ResultLimit = 3

def ProcessUserQuery(QueryString):
    """Queries ChromaDB using the captured user query string."""
    print(f"\nProcessing UQ: '{QueryString}'")
    
    QueryResults = CollectionInstance.query(
        query_texts=[QueryString],
        n_results=ResultLimit
    )
    
    print("--- Search Results ---")
    print(QueryResults)

# Keyboard event loop simulation
def HandleKeyEvent(e):
    global CurrentBuffer
    
    if e.name == 'enter':
        QueryString = "".join(CurrentBuffer)
        ProcessUserQuery(QueryString)
        CurrentBuffer = []  # Reset buffer
    elif e.name == 'backspace':
        if CurrentBuffer:
            CurrentBuffer.pop()
    elif e.name == 'space':
        CurrentBuffer.append(" ")
    elif len(e.name) == 1:
        CurrentBuffer.append(e.name)