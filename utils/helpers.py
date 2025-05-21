# utils/helpers.py

def clean_text(text: str) -> str:
    """
    Lowercases and strips whitespace from input text.

    Args:
        text (str): Input string

    Returns:
        str: Cleaned text
    """
    return text.strip().lower()
