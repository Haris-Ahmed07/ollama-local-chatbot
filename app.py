# backend.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)

chat_history = [
    {
        "role": "system",
        "content": (
            "You are a helpful and intelligent personal AI assistant. "
            "Answer all questions clearly, politely, and concisely. Limit responses to 2 lines."
        )
    }
]

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")

    chat_history.append({"role": "user", "content": user_message})

    try:
        response = ollama.chat(model="qwen2.5-coder:0.5b", messages=chat_history)
        reply = response['message']['content']
    except Exception as e:
        reply = f"Error: {str(e)}"

    chat_history.append({"role": "assistant", "content": reply})
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
