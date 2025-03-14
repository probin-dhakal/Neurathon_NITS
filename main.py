from flask import Flask, render_template, request, session, send_file, jsonify
from src.helper import download_hugging_face_embeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from fpdf import FPDF
from datetime import datetime
import os
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

embeddings = download_hugging_face_embeddings()
Pinecone(api_key=PINECONE_API_KEY)

index_name = "debate-ai"
docsearch = PineconeVectorStore.from_existing_index(index_name, embeddings)


def main_new(user_query):
    llm = CTransformers(
        model=r"C:\Users\Asus\Desktop\Debate_ai_1\llama-2-7b-chat.ggmlv3.q2_K.bin",
        model_type="llama",
        config={'max_new_tokens': 2000, 'temperature': 0.8}
    )
    print("Model loaded successfully.")

    # Correct prompt template
    prompt_template = """You are a debate agent. Use the context below to respond.
    Context: {context}
    Provide a detailed and helpful response in one line."""
    
    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context"]
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=docsearch.as_retriever(search_kwargs={'k': 1}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )

    result = qa.invoke({"query": user_query})

    return result["result"]


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


# if __name__ == "__main__":
#     print(main_new("What is debate"))

    
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

    ai_response = main_new(initial_argument)

    return jsonify({'response': ai_response})

@app.route('/get', methods=['POST'])
def chat():
    user_query = request.json.get('message')
    #print(user_query)
    response = main_new(user_query)
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
