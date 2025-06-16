def moderate_response(response):
    banned_phrases = [
        "you should", "you must", "I suggest", "take medicine", "consult a doctor"
    ]
    for phrase in banned_phrases:
        if phrase in response.lower():
            return "I'm here to listen. Please know you're not alone."
    return response
