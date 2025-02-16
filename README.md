# Debate Partner AI

## Overview
This is a Flask-based web application that allows users to engage in a debate with an AI agent. It tracks the conversation history and provides the option to download the debate transcript as a PDF.

## Features
- Start a debate with an AI agent.
- Real-time conversation with an AI opponent.
- Conversation history displayed on the web interface.
- Download the debate transcript as a PDF.
- Pinecone vector search integration.
- Gemini API for AI-generated responses.

## Requirements
- Python 3.8+
- Flask
- OpenAI library
- ReportLab
- Pinecone-client
- Google Generative AI API (Gemini)

## Installation
1. Clone this repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate into the project directory:
   ```bash
   cd Debate_ai_1/Neurathon_NITS
   ```
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
4. Activate the virtual environment:
   - Windows:
     ```bash
     ..\..\.venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     ../../.venv/bin/activate
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Create a `.env` file in the project root directory with the following content:
```
PINECONE_API_KEY=your_pinecone_api_key
GOOGLE_API_KEY=your_gemini_api_key
```

## Usage
1. Run the Flask application:
   ```bash
   python main.py
   ```
2. Access the application in your browser:
   - [http://127.0.0.1:8081](http://127.0.0.1:8081)

## Running Logs
Example logs from the Flask application:
```
 * Serving Flask app 'main'
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8081
 * Running on http://192.168.12.129:8081
Press CTRL+C to quit
```

## Generating PDF
Click on the "Download PDF" button after the debate to download the transcript.

## Example Output
```
127.0.0.1 - - [16/Feb/2025 16:05:30] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [16/Feb/2025 16:05:47] "POST /start_debate HTTP/1.1" 200 -
127.0.0.1 - - [16/Feb/2025 16:06:48] "GET /download_pdf HTTP/1.1" 200 -
```

## Troubleshooting
- Ensure all API keys are valid.
- Restart the Flask server if changes are made to the code.
- If any grpc_wait_for_shutdown_with_timeout() errors occur, try rerunning the server.



