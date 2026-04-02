def classify_email(text):
    text = text.lower()

    if "complaint" in text:
        return "complaint"
    elif "urgent" in text or "emergency" in text:
        return "emergency"
    elif "water" in text:
        return "water_issue"
    else:
        return "general"