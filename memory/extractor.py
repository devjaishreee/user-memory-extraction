# memory/extractor.py

# Uses GPT-4 to extract factual memories from a conversation
# In a real system, this would use the OpenAI API to analyze user history

def extract_facts(conversation: str) -> list:
    """
    Extract key factual statements about the user from the conversation.
    For demo purposes, this is hardcoded. Replace with GPT-4 call.
    """
    return [
        "User prefers concise answers",
        "User lives in India",
        "User prefers night-time reminders"
    ]
