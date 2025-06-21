# 🧠 Ollama Local Chatbot (AI Personal Assistant)

A simple and responsive web-based personal AI assistant powered by **Ollama** and **Flask**. This assistant uses the `qwen2.5-coder:0.5b` model locally and responds concisely in under 2 lines.

---

## 🚀 Features

- Simple HTML frontend chat UI
- Fast and local inference via Ollama
- Flask backend with history tracking
- Easily switch to any Ollama-supported model

---

## 🔧 Requirements

- Python 3.8+
- Ollama Desktop (Windows/Mac/Linux)
- ollama model: `qwen2.5-coder:0.5b`

---

## 🛠 Setup Instructions

### 1. Install Ollama and Run the Model

> 📥 First, download and install Ollama Desktop from:  
> 👉 https://ollama.com/download

Then in your terminal or CMD:

```bash
ollama run qwen2.5-coder:0.5b
````

* This will **download the model** (if not already) and start the local LLM server.
* Once downloaded, it will **automatically run** the model.
* To stop chatting, type `/bye` in the Ollama terminal.

You can list all downloaded models with:

```bash
ollama list
```

---

### 2. Clone This Repository

```bash
git clone https://github.com/Haris-Ahmed07/ollama-local-chatbot.git
cd ollama-local-chatbot
```

---

### 3. Create and Activate a Virtual Environment (Recommended)

#### On **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

#### On **macOS/Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install Python Requirements

```bash
pip install -r requirements.txt
```

---

### 5. Run the Flask App

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

You can now chat with your own personal assistant in the browser!

---

## 🎨 Customize It

You can **replace `qwen2.5-coder:0.5b`** with any other Ollama-supported model (like `llama3`, `mistral`, etc.) for improved performance or different personalities.

Simply update this line in `app.py`:

```python
response = ollama.chat(model="your_model_here", messages=chat_history)
```

---

## 📁 Project Structure

```
ollama-local-chatbot/
│
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
└── templates/
    └── index.html          # Simple responsive frontend
```

---

## 💬 Example Prompt

> "What’s the best way to build muscle fast?"

**Assistant:**

> "Lift heavy weights, focus on compound exercises. Eat protein-rich food."

---

## ✅ You're All Set!

Enjoy your lightweight, privacy-friendly **local AI assistant** — completely running on your machine. 🎉
