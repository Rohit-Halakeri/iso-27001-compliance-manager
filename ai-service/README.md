# Tool-14 — AI Service

AI microservice for ISO 27001 Compliance Manager built with Flask and Groq API.

## Prerequisites

- Python 3.11+
- pip

## Setup Steps

Step 1 — Clone the repository:

git clone https://github.com/tecsxpert/iso-27001-compliance-manager
cd iso-27001-compliance-manager/ai-service

Step 2 — Create virtual environment:

python -m venv venv
venv\Scripts\activate

Step 3 — Install dependencies:

pip install -r requirements.txt

Step 4 — Create .env file:

GROQ_API_KEY=your_groq_api_key_here

Step 5 — Run the service:

python app.py

Service runs on http://127.0.0.1:5000

## Environment Variables

| Variable | Description | Required |
|---|---|---|
| GROQ_API_KEY | Groq API key from console.groq.com | Yes |

## API Endpoints

GET /health — Returns service health status

Response:
{"status": "ok", "service": "Tool-14 AI Service", "version": "1.0.0"}

POST /sanitise-test — Tests input sanitisation middleware

Request: {"text": "Your input text here"}

Response 200: {"message": "Input is clean and safe", "sanitised_data": {"text": "Your input"}}

Response 400: {"error": "Invalid input detected", "message": "Your input contains prohibited patterns"}

POST /generate-report — Generates compliance report. Rate limited to 10 req/min.

Request: {"data": "compliance data here"}

Response: {"message": "Report generation endpoint", "status": "ok"}

Response 429: {"error": "Rate limit exceeded", "message": "Too many requests", "retry_after": "10 per 1 minute"}

## Security Features

- Input sanitisation — HTML stripping and prompt injection detection
- Rate limiting — 30 req/min default, 10 req/min on /generate-report
- Security headers — CSP, X-Frame-Options, X-Content-Type-Options via flask-talisman
- Returns HTTP 400 on injection attempt
- Returns HTTP 429 on rate limit breach

## Tech Stack

- Python 3.11
- Flask 3.x
- flask-limiter
- flask-talisman
- bleach

## Running Tests

python test_sanitise.py
python test_ratelimit.py
python test_security_week1.py
python test_pii_audit.py
python test_week2_signoff.py

## Author

Rohit Mallikarjun Halakeri
AI Developer 3 — Team 7
Tool-14 — ISO 27001 Compliance Manager