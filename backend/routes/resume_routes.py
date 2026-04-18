from flask import Blueprint, request, jsonify
import os

from services.resume_parser import extract_text
from services.skill_extractor import extract_skills
from services.scoring_engine import calculate_score
from services.feedback_engine import generate_feedback
from services.interview_engine import generate_questions
from services.job_recommender import recommend_job

resume_bp = Blueprint("resume_bp", __name__)

UPLOAD_FOLDER = "backend/uploads"


@resume_bp.route("/upload", methods=["POST"])
def upload_resume():

    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)   # ✅ FIX (important)
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    text = extract_text(filepath)
    skills = extract_skills(text)

    score = calculate_score(text, skills)
    feedback = generate_feedback(text, skills)
    questions = generate_questions(skills)
    job_role = recommend_job(skills)

    # DEBUG
    print("SKILLS:", skills)
    print("QUESTIONS:", questions)
    print("JOB ROLE:", job_role)

    return jsonify({
        "filename": file.filename,
        "extracted_text": text,
        "skills_found": skills,
        "score": score,
        "feedback": feedback,
        "interview_questions": questions,
        "job_role": job_role
    })