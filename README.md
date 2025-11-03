# Dad Joke API 🤖

A lightweight web service built with **FastAPI** that delivers random dad jokes through a simple REST API.  
The project also demonstrates automated deployment to an **AWS EC2** instance using GitHub Actions and webhook integration, highlighting modern DevOps practices in a compact and maintainable architecture.

---

## 🧠 Overview

The Dad Joke API provides a single endpoint, `/joke`, that retrieves and returns random jokes from the public [icanhazdadjoke](https://icanhazdadjoke.com/) API.  
The service is designed for clarity, reliability, and easy deployment to cloud environments.

The repository also includes an automated deployment workflow and a webhook listener that allow the EC2 instance to update itself upon new commits.  
Together, these components model a streamlined, real-world deployment pipeline for small-scale APIs.

---

## ⚙️ Architecture

### API Service (`main.py`)
- Built using **FastAPI** and **HTTPX**
- Sends HTTP requests to the icanhazdadjoke API
- Returns the response as structured JSON:
  ```json
  { "joke": "Why did the scarecrow win an award? Because he was outstanding in his field!" }
### Webhook Service (webhook.py)
Defines a /webhook endpoint that handles GitHub push events

Executes a git pull command on the EC2 instance when updates are pushed to the repository

Can be configured to restart the running service automatically for seamless updates

### Deployment Workflow
Hosted on AWS EC2 using a systemd service running Uvicorn

Supports continuous deployment through:

GitHub Actions (.github/workflows/deploy.yml)

Webhook-triggered updates from GitHub

## 🧰 Tech Stack
Python 3.9+

FastAPI — web framework

Uvicorn — ASGI application server

HTTPX — HTTP client

AWS EC2 — hosting environment

GitHub Actions — CI/CD automation

## 🚀 Local Setup

**Clone the repository:**

git clone https://github.com/<your-username>/ec2api.git

cd ec2api

**Install dependencies:**
pip install -r requirements.txt

**Start the application:**

uvicorn main:app --reload

**Access the API locally:**

http://127.0.0.1:8000/joke

## 🎯 Key Learning Objectives
Building and deploying a production-ready API using FastAPI

Consuming external APIs using HTTPX

Hosting Python applications on AWS EC2

Implementing automated deployments via GitHub Actions and webhooks

Managing persistent services with systemd

## 🙏 Acknowledgments

- **[FastAPI](https://fastapi.tiangolo.com/)** — for providing the high-performance Python web framework used in this project.  
- **[icanhazdadjoke](https://icanhazdadjoke.com/)** — for the public joke API that powers the `/joke` endpoint.  

### 📜 License
MIT License
