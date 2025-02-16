
from flask import Flask, render_template, request, session, send_file, jsonify
from src.helper import download_hugging_face_embeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import google.generativeai as genai
from src.prompt import prompt_template
from fpdf import FPDF
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

embeddings = download_hugging_face_embeddings()
Pinecone(api_key=PINECONE_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)

index_name = "debate-ai"
docsearch = PineconeVectorStore.from_existing_index(index_name, embeddings)

PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question", "conversation_history"])

def query_pinecone(user_query):
    search_results = docsearch.similarity_search(user_query, k=10)
    context_texts = [doc.page_content for doc in search_results]
    context_combined = '\n\n'.join(context_texts)
    return context_combined

def main(user_query):
    if 'conversation_history' not in session:
        session['conversation_history'] = []

    conversation_history_text = "\n".join(
        [f"{entry['role']}: {entry['content']}" for entry in session['conversation_history']]
    )

    context_combined = query_pinecone(user_query)

    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = PROMPT.format(
        context=context_combined,
        question=user_query,
        conversation_history=conversation_history_text
    )
    response = model.generate_content(prompt).text

    session['conversation_history'].append({"role": "User", "content": user_query})
    session['conversation_history'].append({"role": "Debate Agent", "content": response})
    session.modified = True

    return response

def generate_pdf(debate_history):
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
    return pdf_file_path


@app.route("/")
def index():
    return render_template('chat2.html')

@app.route('/start_debate', methods=['POST'])
def start_debate():
    data = request.get_json()
    topic = data['topic']
    initial_argument = data['argument']

    session['conversation_history'] = []
    session['conversation_history'].append({"role": "User", "content": f"Debate Topic: {topic}"})
    session['conversation_history'].append({"role": "User", "content": f"Initial Argument: {initial_argument}"})

    ai_response = main(initial_argument)

    return jsonify({'response': ai_response})

@app.route('/get', methods=['POST'])
def chat():
    user_query = request.json.get('message')
    #print(user_query)
    response = main(user_query)
    return jsonify({'response': response})

@app.route('/download_pdf')
def download_pdf():
    debate_history = session.get('conversation_history', [])
    if not debate_history:
        return "No debate history available to download.", 400

    pdf_path = generate_pdf(debate_history)
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)
