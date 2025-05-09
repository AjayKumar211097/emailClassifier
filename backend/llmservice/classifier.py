# backend/llmservice/classifier.py

def classify_description(description: str) -> str:
    """
    Dummy LLM-based classifier.
    Tags as 'Critical' if certain keywords appear.
    """
    text = description.lower()
    if any(k in text for k in ["outage", "fiber cut", "major"]):
        return "Critical"
    return "Informational"
