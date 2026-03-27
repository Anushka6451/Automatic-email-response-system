def generate_response(category):
    responses = {
        "complaint": "We have received your complaint. Our team will resolve it soon.",
        "emergency": "Your issue is urgent. Immediate action is being taken.",
        "water_issue": "Water department has been notified.",
        "general": "Thank you for contacting us. We will get back to you soon."
    }

    return responses.get(category, "Thank you for reaching out.")