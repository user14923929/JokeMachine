from flask import Flask, jsonify
from random import choice

app = Flask(__name__)
app.json.ensure_ascii = False

jokes = (
    {
        "setup": "Why do programmers prefer dark mode?",
        "delivery": "Because light attracts bugs. 🐞"
    },
    {
        "setup": "I told my Wi-Fi we need to talk.",
        "delivery": "Now it’s ignoring me even harder. 📶"
    },
    {
        "setup": "Why don’t robots ever get tired?",
        "delivery": "They recharge instead of overthinking. 🤖"
    },
    {
        "setup": "My phone battery and my motivation have one thing in common:",
        "delivery": "They both drop to 1% at the worst possible moment. 🔋"
    },
    {
        "setup": "I tried to be productive today.",
        "delivery": "My brain said: “Trial version expired.” 🧠"
    }
)

@app.route("/")
def index():
    joke = choice(jokes)
    return jsonify([
        {"type": "setup", "text": joke["setup"]},
        {"type": "delivery", "text": joke["delivery"]},
    ])

