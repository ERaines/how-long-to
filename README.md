# how-long-to

A simple countdown web app and API built with Python (Flask), containerized with Docker, and deployed on Render.
It calculates how much time is left (or elapsed) until a specific date/event in any timezone.

Live Demo: [how-long-to.onrender.com](https://how-long-to.onrender.com/)

<img src="https://github.com/ERaines/how-long-to/blob/main/WEB/image/Screenshot%202025-08-20%20184909.png?raw=true" 
     alt="Imagem de How long to" width="150"/>


## About the Project

This project was developed with the goal of understanding the entire process of building an application — from creating an API to integrating it with the front end and publishing it online.

The idea wasn’t to build something complex, but rather to go through the key stages involved in a complete project. I used this process as a hands-on learning experience, exploring tools I wasn’t very familiar with. While I already had a solid foundation in Python, it was my first time working with technologies like Flask and Docker.

I also had the chance to revisit JavaScript and HTML concepts, which I hadn’t used in a while, and to strengthen my command of Git through version control and code organisation.

As for next steps, I plan to optimise the project, as I know there are plenty of improvements that can be made. Still, it’s already served its main purpose: in the absence of a technical team to collaborate with or guide me, I managed to structure and complete a project on my own, learning through both the mistakes and the wins along the way.


## Features

Countdown API: returns days/hours/minutes/seconds until an event.

Timezone support (IANA tz database, via tzdata).

Frontend: lightweight HTML + JavaScript interface, served by Flask.

Dockerized: portable, production-ready setup with Gunicorn.

Deploy: running on Render



## Tech Stack

Backend: Flask + flask-cors + python-dateutil + tzdata

Frontend: Static HTML + JavaScript (served via Flask)

Container: Docker + Gunicorn

Deploy: Render Web Service (Docker runtime)

Version Control: Git + GitHub

Running locally
Prerequisites

Python 3.11+

Git

Docker (optional for containerized run)

Virtual environment setup
python -m venv .venv
.venv\Scripts\activate    # Windows
source .venv/bin/activate  # Linux/Mac

pip install -r requirements.txt

Run the API
python app.py


→ available at http://127.0.0.1:8000

Run the frontend

Option A: open api/static/index.html directly in your browser.
Option B: serve it with Python:

cd api/static
python -m http.server 5500

Docker (alternative run)
cd api
docker build -t how-long-to .
docker run -p 8000:8000 how-long-to

Tests
cd api
pytest -q


PS: This project was created with the aim of understanding the entire process of putting an API online, and it was developed with the help of an AI.
