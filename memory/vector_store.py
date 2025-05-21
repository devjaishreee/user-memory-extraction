# memory/vector_store.py

import faiss
import numpy as np

class MemoryStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)  # L2 (Euclidean) distance search
        self.facts = []  # Store corresponding text facts for each embedding

    def add(self, vector: np.ndarray, fact: str):
        """
        Add a single fact embedding and its text to the store.
        """
        self.index.add(np.array([vector]).astype('float32'))
        self.facts.append(fact)

    def query(self, vector: np.ndarray, k: int = 3) -> list:
        """
        Return top-k similar facts for a given query vector.

        Args:
            vector (np.ndarray): Embedded query.
            k (int): Number of closest matches to return.

        Returns:
            list: List of top-k matching factual memories.
        """
        if len(self.facts) == 0:
            return []
        D, I = self.index.search(np.array([vector]).astype('float32'), k)
        return [self.facts[i] for i in I[0] if i < len(self.facts)]
