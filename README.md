# 🤖 AI Resume Analyzer & Job Recommendation System

An intelligent AI-powered web application that analyzes resumes, extracts skills, calculates ATS score, generates feedback, recommends job roles, and prepares interview questions — all in real-time.

---

## 🚀 Project Overview

This project is built to solve a real-world problem:  
👉 Students and job seekers often don’t know how strong their resume is or what roles they fit best for.

So, this system acts like an **AI career advisor** that:

- Parses resumes (PDF/Text)
- Extracts skills automatically
- Calculates ATS (Applicant Tracking System) score
- Generates detailed feedback
- Recommends suitable job roles
- Produces interview questions based on skills

---

## 💡 Problem Statement

Many candidates struggle with:
- Poor resume formatting
- Lack of skill awareness
- No idea about job suitability
- No interview preparation guidance

👉 This project solves all of these using automation and AI logic.

---

## ⚙️ Key Features

### 📄 Resume Processing
- Upload resume (PDF/Text)
- Extract raw text automatically

### 🧠 AI Skill Extraction
- Detects technical and soft skills
- Filters relevant keywords from resume

### 📊 ATS Score Generator
- Scores resume based on structure + skills
- Simulates real ATS system behavior

### 💬 Smart Feedback System
- Strengths analysis
- Weakness identification
- Improvement suggestions

### 💼 Job Role Recommendation
- Suggests best-fit job roles based on skills
- Example: Python Developer, Data Analyst, etc.

### 🧠 Interview Question Generator
- Generates role-based interview questions
- Helps in interview preparation

---

## 🏗️ Tech Stack

### Backend
- Python 🐍
- Flask 🌐
- File Handling (OS module)

### AI/Logic Layer
- Custom NLP-based skill extractor
- Rule-based recommendation engine

### Frontend
- HTML5
- CSS3
- JavaScript

---

## 📁 Project Structure


#### backend/
#### │
#### ├── app.py
#### ├── routes/
#### │ └── resume_routes.py
#### │
#### ├── services/
#### │ ├── resume_parser.py
#### │ ├── skill_extractor.py
#### │ ├── scoring_engine.py
#### │ ├── feedback_engine.py
#### │ ├── interview_engine.py
#### │ └── job_recommender.py
#### │
#### └── uploads/

#### frontend/
#### │
#### ├── index.html
#### ├── upload.html
#### ├── dashboard.html
#### ├── css/
#### └── js/


---

## 🔄 System Workflow


User uploads Resume
↓
Flask Backend receives file
↓
Text extraction from resume
↓
Skill extraction engine runs
↓
ATS score calculation
↓
Feedback generation
↓
Job role recommendation
↓
Interview questions generation
↓
Frontend displays results


---

## 🧪 How to Run the Project

### 1️⃣ Clone Repository
bash
git clone https://github.com/Hanshika103/AI-Resume-Analysis---Job-Creation.git
cd ai-resume-analyzer
### 2️⃣ Install Dependencies
pip install flask
### 3️⃣ Run Backend
python app.py
### 4️⃣ Open Frontend
Open index.html in browser
OR
Run using Live Server (VS Code)
### 📸 Screenshots

#### Landing Page
```
<img width="1158" height="471" alt="loaded" src="https://github.com/user-attachments/assets/6273625a-a3f2-47e3-904c-6df0a8363104" />

```
### Upload Page
```
<img width="959" height="513" alt="uploaded" src="https://github.com/user-attachments/assets/b9237cc8-81e2-449e-b6d6-ad8366893d41" />

```

### Dashboard Result Page
```
<img width="681" height="621" alt="dashboard1" src="https://github.com/user-attachments/assets/6848ad45-78b8-49df-a1a5-5df3811b8adc" />

<img width="457" height="611" alt="dashboard2" src="https://github.com/user-attachments/assets/bc727e8e-46ea-4879-b80f-fcbc668e0c0c" />


```

## 🎯 Future Improvements
### 🔥 AI-based LLM integration (OpenAI/HuggingFace)
### 📊 Advanced ATS scoring model
### 📄 PDF report download feature
### 🌐 Deployment on cloud (Render / Vercel)
### 📱 Mobile responsive optimization
## 🧠 Learning Outcomes

### This project helped in understanding:

### Flask backend development
### File upload handling
### Basic NLP concepts
### Full-stack integration
### Real-world AI workflow design
## 👨‍💻 Author

### Hanshika Mukati

### Passionate about AI + Web Development
### Building real-world projects for learning & placements
## ⭐ If you like this project

## Give it a ⭐ on GitHub and share it with others!
