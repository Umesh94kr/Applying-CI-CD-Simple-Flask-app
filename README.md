## This projects shows how to work with github actions adding CI/CD

# 🚀 Flask App — CI/CD, Docker & Automated Testing

This project is a simple yet production-ready **Flask application** that demonstrates:
- Building REST APIs in Python (Flask)
- Docker containerization for easy deployment
- GitHub Actions CI - CD pipeline for automated testing with `pytest` and deployment
- Clean and modular project structure

---

## 🧠 Overview

This repository is meant to show how to:
- Develop and test a Flask app locally  
- Run the same app inside a Docker container  
- Automate testing and deployment using GitHub Actions  
- Push the image to Docker Hub (`umeshkr/flask-app`)

---

## 📁 Project Structure
```````
flask-app/
├── .gitignore # Files/folders to ignore (e.g., venv, pycache)
├── app.py # Flask application entry point
├── requirements.txt # Python dependencies
├── Dockerfile # Docker image instructions
├── test_app.py # Unit tests using pytest
├── .github/
│ └── workflows/
│ └── ci_cd.yml # GitHub Actions workflow (CI/CD)
└── README.md # Project documentation
```````


## ⚙️ Setup and Run Locally

### 1️⃣ Clone this repository
```bash
git clone https://github.com/Umesh94kr/Applying-CI-CD-Simple-Flask-app.git
cd flask-app
```
### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the Flask app 
```bash
python app.py
```
Your app should now be running at:
👉 http://127.0.0.1:5000

## 🏗️ Build Docker Image
```bash
docker build -t flask-app .
### Run the container
docker run -p 5000:5000 flask-app
```

## 📦 Pull Prebuilt Image (from Docker Hub)
```bash
docker pull --platform linux/amd64 umeshkr/flask-app
docker run --platform linux/amd64 -p 5000:5000 umeshkr/flask-app
```

