# demo/retrieval_demo.py

from memory.extractor import extract_facts
from memory.embedder import embed_text
from memory.vector_store import MemoryStore

# Step 1: Initialize vector store
store = MemoryStore(dim=384)

# Step 2: Load example conversation
with open("demo/example_conversations.txt") as f:
    conversation = f.read()

# Step 3: Extract factual memories using GPT-4 mock
facts = extract_facts(conversation)

# Step 4: Embed and store each fact
for fact in facts:
    vector = embed_text(fact)
    store.add(vector, fact)

# Step 5: User makes a query
query = "What time should I notify the user?"

# Step 6: Embed query and retrieve relevant memories
query_vec = embed_text(query)
results = store.query(query_vec)

# Step 7: Show results
print("\nQuery:", query)
print("Relevant Memories:")
for i, memory in enumerate(results, 1):
    print(f"{i}. {memory}")
