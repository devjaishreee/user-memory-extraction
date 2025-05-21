# memory/embedder.py

from sentence_transformers import SentenceTransformer

# Load the SBERT model for text embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text: str):
    """
    Converts a string into a vector embedding.
    
    Args:
        text (str): Input sentence or fact.

    Returns:
        numpy.ndarray: 384-dimensional embedding vector.
    """
    return model.encode(text)
