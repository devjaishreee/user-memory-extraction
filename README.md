# User Memory Extraction System using GPT-4 + FAISS
This project implements a long-term factual memory system for AI agents by extracting key user information from conversation history using GPT-4 and storing it in a scalable vector database (FAISS). The system captures persistent user traits—like preferences, routines, and constraints—and enables personalized, context-aware responses across sessions.

Using semantic embeddings from Sentence-BERT, extracted facts are stored and retrieved via FAISS for fast similarity search. When a new user query arrives, relevant memory is dynamically injected into the prompt, allowing the AI agent to “remember” the user.

Built With
GPT-4 – for high-precision factual extraction
Sentence-BERT – to embed user facts and queries
FAISS – for fast and scalable vector similarity search
Python – core implementation
Dotenv – to manage OpenAI API credentials

