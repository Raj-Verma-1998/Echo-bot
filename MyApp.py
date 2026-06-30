from flask import Flask, request, render_template, jsonify
from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv
import nltk

load_dotenv()

# Instantiate the OpenAI client
client = OpenAI()
app = Flask(__name__, template_folder="templates")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# NLP setup (used for lightweight text preprocessing / intent matching)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')

SYSTEM_PROMPT = (
    "You are Echo-Bot, a friendly and helpful general-purpose AI assistant. "
    "Answer the user's questions clearly and concisely."
)


@app.route('/')
def home():
    return render_template('try.html')


@app.route('/messager', methods=['POST'])
def messager():
    user_msg = request.get_json()['message']
    bot_response = ""

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_msg}
            ]
        )
        bot_response = completion.choices[0].message.content.strip()

    except OpenAIError as e:
        print(f"OpenAI API Error: {e}")
        bot_response = "I'm currently having some trouble. Please try again later."

    return jsonify({"response": bot_response})


if __name__ == '__main__':
    app.run(debug=True)
