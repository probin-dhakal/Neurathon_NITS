# Debate Partner AI

## Overview
This is a Flask-based web application that allows users to engage in a debate with an AI agent. It tracks the conversation history and provides the option to download the debate transcript as a PDF.

## Motivation
The motivation behind this project is to create an interactive AI-driven debate partner that helps users improve their argumentation and critical thinking skills. This project was built to explore the capabilities of Natural Language Processing (NLP) models in real-time conversations.

## Problem Solved
Often, individuals lack a platform to practice debates and improve their articulation. This AI-powered debate platform offers a personalized debating experience anytime, anywhere.

## Learning Outcomes
- Integration of NLP models into a web application.
- Working with vector embeddings and similarity search.
- Using Hugging Face's Sentence Transformers and Pinecone for semantic search.
- Leveraging the LLaMA model for generating contextual AI responses.

## Features
- Start a debate with an AI agent.
- Real-time conversation with an AI opponent.
- Conversation history displayed on the web interface.
- Download the debate transcript as a PDF.
- Pinecone vector search integration for semantic similarity.
- LLaMA model for AI-generated responses.

## Table of Contents
- Overview
- Motivation
- Problem Solved
- Learning Outcomes
- Features
- Requirements
- Installation
- Configuration
- Usage
- Underlying Concepts
- Generating PDF
- Running Logs
- Troubleshooting
- Credits
- License

## Requirements
- Python 3.10+
- Flask
- OpenAI library
- ReportLab
- Pinecone-client
- Hugging Face Transformers
- Sentence Transformers

## Installation
Clone this repository:
```sh
git clone <repository_url>
```

Navigate into the project directory:
```sh
cd Debate_ai_1/
```

Create a virtual environment:
```sh
python -m venv .venv
```

Activate the virtual environment:

**Windows:**
```sh
.venv\Scripts\activate
```

**Linux/Mac:**
```sh
source .venv/bin/activate
```

Install dependencies:
```sh
pip install -r requirements.txt
```

## Configuration
Create a `.env` file in the project root directory with the following content:
```sh
PINECONE_API_KEY=your_pinecone_api_key
```

## Usage
Run the Flask application:
```sh
python main.py
```

Access the application in your browser:
```
http://127.0.0.1:8081
```

## Underlying Concepts
### Vector Embedding with Pinecone and Sentence Transformers
We use Sentence Transformers from Hugging Face to convert user queries and text into vector embeddings. These embeddings represent the semantic meaning of the text, allowing us to perform similarity searches efficiently.

The generated embeddings are indexed and stored in Pinecone, a vector search database. When a new query is made, its embedding is compared with the stored embeddings to retrieve the most relevant information based on semantic similarity.

### Language Model - LLaMA
We leverage Meta's LLaMA model as the core language model to generate contextually accurate responses during debates. The retrieved relevant information from Pinecone is passed as context to the LLaMA model, improving the quality of generated responses.

## Generating PDF
Click on the "Download PDF" button after the debate to download the transcript.

## Running Logs
Example logs from the Flask application:
```
Serving Flask app 'main'
Debug mode: on
Running on all addresses (0.0.0.0)
Running on http://127.0.0.1:8081
Running on http://192.168.12.129:8081 Press CTRL+C to quit
```

## Troubleshooting
- Ensure Pinecone API keys are valid.
- Restart the Flask server if changes are made to the code.
- If any `grpc_wait_for_shutdown_with_timeout()` errors occur, try rerunning the server.

## Credits
- **Developer:** Team 0101 NEURATHON NIT Silchar
- **Hugging Face:** Sentence Transformers
- **Pinecone:** Vector Search
- **Meta:** LLaMA Model

## License
This project is licensed under the MIT License.


![nlp](https://github.com/user-attachments/assets/e01ec5ab-6b8c-4da3-954c-00b573843e4a)


