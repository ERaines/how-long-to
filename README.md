📌 how-long-to

A simple countdown web app and API built with Python (Flask), containerized with Docker, and deployed on Render.
It calculates how much time is left (or elapsed) until a specific date/event in any timezone.

🔗 Live Demo: how-long-to.onrender.com

✨ Features

🕒 Countdown API: returns days/hours/minutes/seconds until an event.

🌍 Timezone support (IANA tz database, via tzdata).

⚡ Frontend: lightweight HTML + JavaScript interface, served by Flask.

🐳 Dockerized: portable, production-ready setup with Gunicorn.

☁️ Deploy: running on Render
.

🚀 Endpoints
Health check
GET /health


Response:

{"status": "ok"}

Countdown
GET /countdown?date=2025-12-25&title=Christmas&tz=Europe/Dublin


Response:

{
  "title": "Christmas",
  "target": "2025-12-25T00:00:00+00:00",
  "now": "2025-08-20T15:00:00+00:00",
  "timezone": "Europe/Dublin",
  "total_seconds": 10944000,
  "past": false,
  "breakdown": {
    "days": 126,
    "hours": 12,
    "minutes": 0,
    "seconds": 0
  },
  "message": "Remaining 126d 12h 0m 0s until Christmas"
}

🛠️ Tech Stack

Backend: Flask + flask-cors + python-dateutil + tzdata

Frontend: Static HTML + JavaScript (served via Flask)

Container: Docker + Gunicorn

Deploy: Render Web Service (Docker runtime)

Version Control: Git + GitHub

🧑‍💻 Running locally
Prerequisites

Python 3.11+

Git

Docker (optional for containerized run)

Virtual environment setup
python -m venv .venv
.venv\Scripts\activate    # Windows
# source .venv/bin/activate  # Linux/Mac

pip install -r requirements.txt

Run the API
python app.py


→ available at http://127.0.0.1:8000

Run the frontend

Option A: open api/static/index.html directly in your browser.
Option B: serve it with Python:

cd api/static
python -m http.server 5500

🐳 Docker (alternative run)
cd api
docker build -t how-long-to .
docker run -p 8000:8000 how-long-to

✅ Tests
cd api
pytest -q


📜 License

MIT License. Free to use, modify, and share.

PS: This project was created with the aim of understanding the entire process of putting an API online, and it was developed with the help of an AI.
