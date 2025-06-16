from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="bhadresh-savani/distilbert-base-uncased-emotion")

def detect_emotion(text):
    result = classifier(text)[0]
    return result['label']