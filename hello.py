from flask import Flask, render_template, request, session, jsonify, send_file
from fpdf import FPDF
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route("/")
def index():
    return render_template('chat2.html')

@app.route('/start_debate', methods=['POST'])
def start_debate():
    data = request.get_json()
    topic = data.get('topic')
    role = data.get('role')
    initial_argument = data.get('argument')

    session['conversation_history'] = []
    session['conversation_history'].append({"role": "User", "content": f"Debate Topic: {topic}"})
    session['conversation_history'].append({"role": "User", "content": f"Initial Argument: {initial_argument}"})

    # Mock AI response (Replace with your AI logic if needed)
    ai_response = f"I understand your argument for the topic '{topic}' as '{initial_argument}'. Let's debate!"

    session['conversation_history'].append({"role": "Debate Agent", "content": ai_response})

    return jsonify({'response': ai_response})

@app.route('/get', methods=['POST'])
def chat():
    data = request.get_json()
    user_query = data.get('msg')

    # Mock AI response (Replace with your AI logic if needed)
    ai_response = f"AI Response to: {user_query}"

    session['conversation_history'].append({"role": "User", "content": user_query})
    session['conversation_history'].append({"role": "Debate Agent", "content": ai_response})

    return jsonify({'response': ai_response})

@app.route('/download_pdf')
def download_pdf():
    debate_history = session.get('conversation_history', [])

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Debate Transcript", ln=True, align='C')

    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')

    pdf.ln(10)
    for entry in debate_history:
        pdf.multi_cell(0, 10, txt=f"{entry['role']}: {entry['content']}")

    pdf_file_path = "debate_transcript.pdf"
    pdf.output(pdf_file_path)
    return send_file(pdf_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8082, debug=True)
