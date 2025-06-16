import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_reflection(message, context, emotion):
    prompt = f"""
    You are a compassionate AI assistant trained to provide emotionally supportive reflections. 
    Never offer advice. Do not diagnose. Just reflect empathetically.

    User emotion: {emotion}
    Context summary: {context}
    Current message: "{message}"

    Respond with a calm, affirming tone as a non-clinical support.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an empathetic listener."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )
    return response.choices[0].message['content'].strip()
