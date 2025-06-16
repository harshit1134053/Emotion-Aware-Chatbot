from flask import Flask, request, jsonify
from llm_module import generate_reflection
from emotion_detector import detect_emotion
from filters import moderate_response
from memory import update_memory, fetch_context

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_id = data['user_id']
    message = data['message']

    emotion = detect_emotion(message)
    context = fetch_context(user_id)
    reflection = generate_reflection(message, context, emotion)
    safe_reflection = moderate_response(reflection)

    update_memory(user_id, message, reflection)

    return jsonify({
        'emotion': emotion,
        'response': safe_reflection
    })

if __name__ == '__main__':
    app.run(debug=True)