# 🌾 Echo-Bot — Agriculture AI Chatbot

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)](https://flask.palletsprojects.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--turbo-412991?logo=openai)](https://openai.com)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-46E3B7?logo=render)](https://echo-bot-qflo.onrender.com)

> A domain-specific conversational AI assistant for Indian farmers — powered by GPT-3.5-turbo with real-time weather forecasting and commodity price lookup.

🔗 **Live Demo:** [echo-bot-qflo.onrender.com](https://echo-bot-qflo.onrender.com)

---

## 📌 Overview

Echo-Bot is an agriculture-focused chatbot that helps Indian farmers with:
- Real-time **weather forecasts** for their location
- Live **commodity & market prices** (via Data.gov.in)
- Guidance on **crop selection**, **soil management**, **pest control**, and more
- **Government schemes** and loan information for farmers
- General **agricultural best practices** using GPT-3.5-turbo

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🤖 LLM-Powered Responses | Uses OpenAI GPT-3.5-turbo for intelligent, context-aware answers |
| 🌦️ Weather Forecast | Real-time weather data via OpenWeatherMap API |
| 💰 Commodity Prices | Live market prices from Data.gov.in API |
| 🌱 Agriculture Domain | 15+ intent categories covering all major farming topics |
| 🇮🇳 India-Specific | Covers state-wise crop advice, Kharif/Rabi seasons, govt schemes |
| 🌐 Web Interface | Clean chat UI served via Flask |
| ☁️ Cloud Deployed | Hosted on Render with WSGI server |

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **AI/LLM:** OpenAI GPT-3.5-turbo
- **NLP:** NLTK (tokenizer, POS tagger, WordNet, stopwords)
- **APIs:** OpenWeatherMap, Data.gov.in
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render (via `wsgi.py`)
- **Config:** python-dotenv

---

## 📁 Project Structure

```
Echo-bot/
├── MyApp.py          # Main Flask application & API logic
├── intents.json      # Agriculture chatbot intent dataset (15+ categories)
├── wsgi.py           # WSGI entry point for production deployment
├── requirements.txt  # Python dependencies
└── templates/
    └── try.html      # Frontend chat interface
```

---

## 🧠 Intent Categories

The chatbot handles the following agriculture domains:

- `greeting` — Conversational greetings
- `weather_forecast` — Weather queries
- `crop_prices` — Commodity prices (wheat, rice, cotton, sugarcane, onions)
- `agricultural_techniques` — Farming best practices
- `pest_management` — Pest control and IPM
- `soil_management` — Soil health and erosion prevention
- `irrigation_methods` — Drip, sprinkler, and precision irrigation
- `crop_selection` — Crop selection based on region/season
- `crop_selection_india` — India-specific (North/South, Kharif/Rabi)
- `organic_farming` — Organic and eco-friendly methods
- `livestock_management` — Animal husbandry
- `technology_in_agriculture` — Drones, precision farming, IoT
- `climate_resilient_farming` — Climate change adaptation
- `loans` — Govt subsidies and loan schemes
- `schemes` — PM Fasal Bima Yojana, Kisan Credit Card, etc.
- `farmer_assistance` — General support and guidance

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
WEATHER_API_KEY=your_openweathermap_api_key
DATA_GOV_API_KEY=your_data_gov_in_api_key
```

### 4. Run the app
```bash
python MyApp.py
```

Visit `http://localhost:5000` in your browser.

---

## 🌐 Deployment

The app is deployed on **Render** using `wsgi.py` as the entry point.

```bash
# Production server command
gunicorn wsgi:app
```

---

## 📸 Screenshots

> Chat interface with real-time responses from GPT-3.5-turbo and live API data.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Raj Verma**
- GitHub: [@Raj-Verma-1998](https://github.com/Raj-Verma-1998)
- Project: [Echo-bot](https://github.com/Raj-Verma-1998/Echo-bot)
