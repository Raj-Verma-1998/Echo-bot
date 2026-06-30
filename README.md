# 🤖 Echo-Bot — AI Conversational Chatbot

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)](https://flask.palletsprojects.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--turbo-412991?logo=openai)](https://openai.com)
[![NLTK](https://img.shields.io/badge/NLP-NLTK-lightgreen)](https://www.nltk.org/)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-46E3B7?logo=render)](https://echo-bot-qflo.onrender.com)

> A general-purpose conversational AI chatbot powered by **OpenAI GPT-3.5-turbo**, with an intent-matching layer for common conversational patterns (greetings, thanks, small talk) and a web chat interface.

🔗 **Live Demo:** [echo-bot-qflo.onrender.com](https://echo-bot-qflo.onrender.com)

---

## 📌 Overview

Echo-Bot is a lightweight AI chatbot built with Flask and OpenAI's GPT-3.5-turbo model. It combines simple intent-based responses for common conversational patterns with LLM-powered responses for open-ended questions, making it a flexible starting point for any conversational AI use case.

---

## ✅ Features

| Feature | Description |
|---|---|
| 🤖 LLM-Powered Responses | OpenAI GPT-3.5-turbo for open-ended, natural conversation |
| 💬 Intent-Based Replies | Lightweight intent matching for greetings, thanks, small talk, and FAQs |
| 🌐 Web Chat Interface | Clean chat UI served via Flask |
| ☁️ Cloud Deployed | Hosted live on Render |
| 🧩 Easily Extensible | Add new intents or swap in a different LLM/system prompt for any domain |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask |
| **AI / LLM** | OpenAI GPT-3.5-turbo |
| **NLP** | NLTK (tokenizer, POS tagger, WordNet, stopwords) |
| **Intent Engine** | Custom JSON-based intent matching |
| **Frontend** | HTML, CSS, JavaScript |
| **Deployment** | Render (via `wsgi.py` + Gunicorn) |
| **Config** | python-dotenv |

---

## 📁 Project Structure

```
Echo-bot/
├── MyApp.py            # Main Flask app — routing and GPT integration
├── intents.json         # General-purpose intent dataset (greetings, thanks, small talk, etc.)
├── wsgi.py              # WSGI entry point for Render deployment
├── requirements.txt     # Python dependencies
└── templates/
    └── try.html         # Frontend chat interface
```

---

## 🧠 Intent Categories

```
greeting           → Conversational greetings
goodbye            → Farewell messages
thanks             → Acknowledging thanks
about_bot          → Questions about the bot itself
help               → General help requests
smalltalk          → Casual conversation
unrecognized_input → Graceful fallback response
```

For anything outside these intents, the bot falls back to GPT-3.5-turbo for a natural, open-ended response.

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Raj-Verma-1998/Echo-bot.git
cd Echo-bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key
```

### 4. Run the app
```bash
python MyApp.py
```

Visit `http://localhost:5000` in your browser.

---

## 🌐 Deployment

Deployed on **Render** using Gunicorn as the production WSGI server.

```bash
gunicorn wsgi:app
```

---

## 💬 Sample Conversation

```
User: Hi there!
Bot:  Hello! How can I help you today?

User: What can you do?
Bot:  I'm a conversational AI chatbot. Ask me anything and I'll do my best to help!

User: Can you explain how neural networks work?
Bot:  [GPT-3.5-turbo generates a natural, open-ended response]
```

---

## 👤 Author

**Raj Verma**
- 🔗 GitHub: [@Raj-Verma-1998](https://github.com/Raj-Verma-1998)
- 🌐 Live: [echo-bot-qflo.onrender.com](https://echo-bot-qflo.onrender.com)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
