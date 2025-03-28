# Smart Analytics: AI-Powered Business Insights

## 📌 Project Overview
Smart Analytics is an AI-driven platform that enables businesses to analyze datasets and extract meaningful insights. Built using FastAPI, Streamlit, and LangChain, it allows users to upload CSV datasets, ask business-related questions, and receive AI-generated insights powered by Groq Llama 3.

## 🚀 Features
- **📂 Upload CSV Files:** Users can upload datasets via the UI.

- **🔍 AI-Powered Insights:** Ask business-related questions and get AI-generated responses.

- **📊 Interactive UI:** Built with Streamlit for seamless interaction.

- **⚡ FastAPI Backend:** Handles dataset storage and AI processing.

- **🐳 Dockerized Deployment:** Includes `Dockerfile` and `docker-compose.yml` for easy setup.

- **🔐 Secure API Keys:** Uses GitHub Actions to manage secrets.

---

## 🏗️ Tech Stack

- **Frontend:** Streamlit (Python)

- **Backend:** FastAPI (Python)

- **AI Model:** LangChain with Groq Llama 3

- **Deployment:** Docker, GitHub Actions

---

## 📂 Folder Structure
```
SMART_ANALYTICS/
│── .github/workflows/deploy.yml  # CI/CD Workflow
│── .dockerignore                  # Docker ignore files
│── .gitignore                      # Git ignore files
│── backend.Dockerfile              # Backend Dockerfile
│── frontend.Dockerfile             # Frontend Dockerfile
│── docker-compose.yml              # Docker Compose setup
│── main.py                         # FastAPI Backend
│── app.py                          # Streamlit Frontend
│── requirements.txt                 # Python Dependencies
│── README.md                        # Project Documentation
```

---

## ⚙️ Setup & Installation
### 🔹 Prerequisites
- Python 3.10+
- Docker & Docker Compose
- Groq API Key (Sign up at Groq.ai)

### 🔹 1️⃣ Clone the Repository
```bash
git clone https://github.com/ka1817/AI_for_Smarter_SQL_Analytics.git
cd smart-analytics
```

### 🔹 2️⃣ Set Up Environment Variables
Create a `.env` file in the root directory:
```
GROQ_API_KEY='Private'  # Create your key at https://groq.com```

### 🔹 3️⃣ Install Dependencies

pip install -r requirements.txt
```

### 🔹 4️⃣ Run the Backend (FastAPI)

uvicorn main:app --host 0.0.0.0 --port 4000
```

### 🔹 5️⃣ Run the Frontend (Streamlit)

streamlit run app.py
```

---

## 🐳 Docker Setup

### 🔹 1️⃣ Build & Run Using Docker Compose

docker-compose up --build
```
This will start both the **backend** (FastAPI) and **frontend** (Streamlit) services.

### 🔹 2️⃣ Stop Containers

docker-compose down
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

### 🔹 Automated Workflow
1. **On Push to `main`** → Builds and pushes Docker images.
2. **Uses Secrets (`GROQ_API_KEY`)** for secure deployment.
3. **Deploys to Docker Hub** automatically.

---

🐳 Docker Deployment

1️⃣ Build and Run with Docker Compose 

docker-compose up --build

2️⃣ Pull Pre-built Docker Images

docker pull pranavreddy123/smart-analytics-backend:latest
docker pull pranavreddy123/smart-analytics-frontend:latest


## 🎯 API Endpoints

### 🔹 Upload Dataset
**Endpoint:** `POST /upload/`
- **Description:** Upload a CSV file for analysis.
- **Response:** `{ "message": "File uploaded successfully", "columns": [...] }`

### 🔹 Get Insights

**Endpoint:** `GET /analyze/`
- **Query Param:** `question=your_question_here`
- **Response:** `{ "question": "...", "insights": "..." }`

---

## 📢 Future Enhancements

- ✅ AI-Powered Data Visualization
- ✅ Advanced Trend Analysis
- ✅ Integration with Multiple Data Sources

---
## 📜 License
This project is licensed under the MIT License.

