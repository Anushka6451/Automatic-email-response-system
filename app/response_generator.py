def generate_response(category):
    responses = {
        "refund": "Your refund is being processed.",
        "delivery_issue": "Your order is on the way.",
        "complaint": "We are sorry for the inconvenience.",
        "inquiry": "We will get back to you shortly."
    }
    return responses.get(category, "Thank you for contacting us.")