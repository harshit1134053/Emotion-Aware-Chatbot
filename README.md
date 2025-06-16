# 🧠 Emotion-Aware Chatbot (LLM + Sentiment Reflection)

This project is a multimodal, emotionally intelligent chatbot that generates non-clinical, therapist-aligned reflections using Large Language Models (LLMs) and sentiment analysis. It was built for sensitive use cases such as mental wellness journaling, coaching, and asynchronous therapeutic interactions.

---

## 🎯 Core Features

- **Emotion Detection**: Uses HuggingFace emotion classifier to interpret user tone.
- **LLM-Powered Reflection**: Generates calm, reflective responses using OpenAI GPT.
- **Safety Filters**: Blocks advice-giving, diagnosis, or inappropriate language.
- **User Memory Context**: Maintains lightweight user memory across sessions.
- **REST API**: Flask-powered, ready to integrate into frontend or mobile apps.

---

## 🚀 Project Structure

emotion-aware-chatbot:
├── app.py # Main Flask API endpoint
├── llm_module.py # Prompt design and OpenAI interaction
├── emotion_detector.py # Emotion classification (transformers)
├── filters.py # Content moderation
├── memory.py # Simple in-memory context tracker
├── utils.py # Helpers (text truncation etc.)
├── requirements.txt # Dependencies


---

## 🛠️ Tech Stack

- **LLM**: OpenAI `gpt-3.5-turbo`
- **NLP**: `distilbert-base-uncased-emotion` (HuggingFace)
- **Backend**: Python + Flask
- **AI Tools**: `transformers`, `torch`, `openai`

---

## 🧪 Example API Call

**Endpoint:** `POST /chat`  
**Payload:**
```json
{
  "user_id": "user123",
  "message": "I feel overwhelmed by everything right now."
}

{
  "emotion": "sadness",
  "response": "It sounds like things are really heavy for you right now. I'm here with you."
}

🔒 Safety & Ethical Design
Prompts are explicitly restricted from giving advice or making diagnoses.

Safety filter blocks unsafe language and redirects to neutral support.

Memory is stored per session, and this code is deployable in a secure backend.


📦 Installation

git clone https://github.com/harshit1134053/emotion-aware-chatbot.git
cd emotion-aware-chatbot
pip install -r requirements.txt

Set your OpenAI API key in the environment:
export OPENAI_API_KEY=your_key_here

Run the app:
python app.py

✅ Ideal For
1)AI-enabled journaling or self-reflection tools
2)Mental wellness or behavioral health MVPs
3)Coaches, therapists, and human-in-the-loop systems

📬 Contact
Built by Harshit Mishra

