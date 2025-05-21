# main.py

from memory.extractor import extract_facts
from memory.embedder import embed_text
from memory.vector_store import MemoryStore
from utils.helpers import clean_text

def run_memory_pipeline(conversation: str, query: str):
    print("📥 Conversation:")
    print(conversation)

    # Step 1: Extract factual memory
    facts = extract_facts(conversation)
    print("\n🧠 Extracted Facts:")
    for f in facts:
        print("-", f)

    # Step 2: Embed and store facts
    store = MemoryStore(dim=384)
    for fact in facts:
        vector = embed_text(clean_text(fact))
        store.add(vector, fact)

    # Step 3: Query memory
    print(f"\n🔍 Query: {query}")
    query_vec = embed_text(clean_text(query))
    results = store.query(query_vec)

    print("\n📌 Retrieved Memories:")
    for i, mem in enumerate(results, 1):
        print(f"{i}. {mem}")

if __name__ == "__main__":
    # Example run
    with open("demo/example_conversations.txt") as f:
        conversation = f.read()

    query = "When should I notify the user?"
    run_memory_pipeline(conversation, query)
