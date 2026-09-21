import chromadb
import sys
# import chromadb
import keyboard

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

    if e.name == 'esc':
        print("\nExiting program...")
        keyboard.unhook_all()
        sys.exit(0)
    
    elif e.name == 'enter':
        QueryString = "".join(CurrentBuffer)
        ProcessUserQuery(QueryString)
        CurrentBuffer = []  # Reset buffer
    elif e.name == 'backspace':
        if CurrentBuffer:
            CurrentBuffer.pop()
    elif e.name == 'space':
        CurrentBuffer.append(" ")
        print(" ", end="", flush=True)
    elif len(e.name) == 1:
        CurrentBuffer.append(e.name)
        print(e.name, end="", flush=True)

import traceback

try:
    # Your script contents here...
    print("Running...")
    print("Listening for keyboard input... Type your query and press Enter. (Press ESC to exit)")
    keyboard.on_press(HandleKeyEvent)
    keyboard.wait()

except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()