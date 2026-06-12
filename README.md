# 🌾 Echo-Bot — Agriculture AI Chatbot

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)](https://flask.palletsprojects.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--turbo-412991?logo=openai)](https://openai.com)
[![NLTK](https://img.shields.io/badge/NLP-NLTK-lightgreen)](https://www.nltk.org/)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-46E3B7?logo=render)](https://echo-bot-qflo.onrender.com)

> A domain-specific conversational AI chatbot built for Indian farmers — powered by **OpenAI GPT-3.5-turbo** with 20+ agriculture intent categories covering crops, soil, irrigation, pest control, livestock, government schemes, and more.

🔗 **Live Demo:** [echo-bot-qflo.onrender.com](https://echo-bot-qflo.onrender.com)

---

## 📌 Overview

Echo-Bot is an agriculture-focused intelligent chatbot designed to assist Indian farmers with everyday farming queries. It uses a hybrid approach — **intent matching** for structured agriculture responses and **GPT-3.5-turbo** as a fallback for open-ended questions.

---

## ✅ Working Features

| Feature | Description |
|---|---|
| 🤖 LLM-Powered Responses | OpenAI GPT-3.5-turbo with agriculture-specific system prompt |
| 🌱 Intent-Based QA | 20+ intents covering all major farming domains |
| 💰 Crop Price Info | Wheat, rice, onion, cotton, sugarcane price guidance |
| 🌾 Farming Techniques | Soil prep, crop rotation, yield improvement, harvesting |
| 🐛 Pest Management | IPM — biological, cultural, and chemical methods |
| 🏞️ Soil Management | Fertility, erosion prevention, organic amendments |
| 💧 Irrigation Methods | Drip, sprinkler, precision irrigation guidance |
| 🌿 Organic Farming | Natural pesticides, composting, eco-friendly methods |
| 🐄 Livestock Management | Animal husbandry, nutrition, sustainable practices |
| 🛰️ AgriTech | Drones, precision farming, smart equipment info |
| 🌡️ Climate Resilience | Climate change adaptation, extreme weather guidance |
| 🏦 Govt Schemes & Loans | PM Fasal Bima Yojana, Kisan Credit Card, PM Kisan Samman Nidhi |
| 🇮🇳 India-Specific Crops | North/South India, Kharif/Rabi season recommendations |
| 🌐 Web Interface | Clean chat UI served via Flask |
| ☁️ Cloud Deployed | Hosted live on Render |

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
├── MyApp.py            # Main Flask app — routing, intent matching, GPT integration
├── intents.json        # Agriculture intent dataset (20+ categories, 100+ patterns)
├── wsgi.py             # WSGI entry point for Render deployment
├── requirements.txt    # Python dependencies
└── templates/
    └── try.html        # Frontend chat interface
```

---

## 🧠 Intent Categories (20+)

```
greeting              → Conversational greetings
weather_forecast      → General weather-based farming guidance
crop_prices           → Wheat, rice, onion, cotton, sugarcane pricing
agricultural_techniques → Soil prep, yield, rotation, harvesting
pest_management       → IPM — biological, cultural, chemical
soil_management       → Fertility, erosion, organic amendments
irrigation_methods    → Drip, sprinkler, precision irrigation
crop_selection        → Based on soil, climate, market demand
crop_selection_india  → Kharif/Rabi, North/South India specific
organic_farming       → Natural pesticides, composting
livestock_management  → Animal husbandry and nutrition
technology_in_agriculture → Drones, IoT, precision farming
climate_resilient_farming → Adaptation to extreme weather
loans                 → Subsidies, PM Fasal Bima Yojana
schemes               → Kisan Credit Card, PM Kisan Samman Nidhi
farmer_assistance     → General farming support
unrecognized_input    → Graceful fallback response
```

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

## 💬 Sample Conversations

```
User: What is the best crop for Kharif season?
Bot:  Recommended crops for the Kharif season include rice, maize, and cotton.

User: How do I control pests in my crops?
Bot:  Integrated pest management (IPM) is effective — it combines biological,
      cultural, and chemical methods for sustainable pest control.

User: What government schemes are available for farmers?
Bot:  Key schemes: 1) PM Fasal Bima Yojana - crop insurance,
      2) Kisan Credit Card - easy credit access,
      3) PM Kisan Samman Nidhi - Rs.6000/year direct benefit,
      4) National Horticulture Mission - horticulture support.
```

---

## 👤 Author

**Raj Verma**
- 🔗 GitHub: [@Raj-Verma-1998](https://github.com/Raj-Verma-1998)
- 🌐 Live: [echo-bot-qflo.onrender.com](https://echo-bot-qflo.onrender.com)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
