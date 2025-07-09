from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message'].lower()
    response = "I’m not sure how to respond to that. 🤔"

    # Your chatbot logic
    if 'hello' in user_input or 'hi' in user_input:
        response = "Hello there! 👋"
    elif 'time' in user_input:
        response = str(datetime.now())
    elif 'your name' in user_input:
        response = "I am Chatbot 🤖"
    elif 'who is your creator' in user_input:
        response = "My backend codes were written by Mr. SANJITH. My frontend codes were written by Mr. REGISLIN."
    elif 'your origin' in user_input:
        response = "My origin is from INDIA"
    elif 'say me a joke' in user_input:
        response = "Ananthu mela patha onum theriyala 😂"
    elif 'famous tamil actor' in user_input:
        response = "THALAPATHY VIJAY"
    elif 'famous tamil actors' in user_input:
        response = "Top 5: VIJAY, RAJINIKANTH, SURYA, KAMAL HASSAN, SIVA KARTHIKEYAN"
    elif 'famous rajinikanth dialogue' in user_input:
        response = "NA ORU VATTI SONA, NOORU VATTI SONA MAARI"
    elif 'weather' in user_input:
        response = "I can't access real weather, but it looks nice outside! 🌤️"
    elif 'do you have emotions' in user_input:
        response = "I don't have emotions 🧠"
    elif 'can you sing a song' in user_input:
        response = "NAA ADICHA THAANGA MATA NALU MASAM THOONGA MATA MOTHI PARU VEEDU POI SERA MATA"
    elif 'say me a riddle' in user_input:
        response = "ANJU ADUKU NAALU EDUKU, ATHU ENNA? Answer: VERAL (fingers)"
    elif 'can you rap' in user_input:
        response = " Ulagatharam ullooru vaathiyaaru Thooki pottu saathuvaaru Thatti thatti thookuvaaru Ketta pulla thirunthida Sattam thaanda edam Ulla vanthu thappu senja Vaathi RAIDU varum"
    elif 'bye' in user_input:
        response = "Goodbye! Have a great day! 👋"

    return jsonify({'response': response})
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

