# User Memory Extraction System (LLM + FAISS)

A factual memory system for AI agents that uses GPT-4 to extract user traits (like preferences and routines) from conversations, stores them in a FAISS vector database using Sentence-BERT embeddings, and retrieves relevant memories for personalized, context-aware responses.

---

## Features

- Factual memory extraction via GPT-4
- Embedding-based semantic memory using Sentence-BERT
- Fast vector search with FAISS
- Context injection for dynamic personalization
- Modular, extensible, and ready for production

---

## Tech Stack

- `openai` – GPT-4 for factual extraction
- `sentence-transformers` – SBERT (`all-MiniLM-L6-v2`) for text embeddings
- `faiss-cpu` – Scalable memory retrieval engine
- `python-dotenv` – Secure API key management
- `numpy` – Vector math

---

## Folder Structure

```
user-memory-extraction/
├── main.py                     # Runs the full memory pipeline
├── memory/
│   ├── extractor.py            # GPT-4 based memory extraction
│   ├── embedder.py             # Embedding with SBERT
│   ├── vector_store.py         # FAISS-based vector DB
├── demo/
│   ├── example_conversations.txt  # Sample chat logs
│   └── retrieval_demo.py       # End-to-end demo script
├── utils/
│   └── helpers.py              # Utility functions
├── requirements.txt            # Python dependencies
├── .gitignore                  # Ignored files and secrets
└── README.md                   # Project documentation
```

---

##  Setup & Usage

### 1. Clone and install dependencies
```bash
git clone https://github.com/yourusername/user-memory-extraction.git
cd user-memory-extraction
pip install -r requirements.txt
```

### 2. Add your OpenAI API key
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 3. Run the main pipeline
```bash
python main.py
```

### 4. Sample Output

```
Query: When should I notify the user?
Retrieved Memories:
1. User prefers night-time reminders
```

---

## Demo Input Example

**demo/example_conversations.txt**
```
User: I live in India.
User: Please keep your responses short.
User: I prefer night-time reminders.
```

---

## Use Cases

- AI Assistants with memory
- Personalized chatbots
- Long-term user modeling
- Conversational agents in mental health, education, and productivity tools

---

## Notes

- This project uses GPT-4 via OpenAI’s API. Ensure you have access.
- Do **not** commit your `.env` file or API key.

---
