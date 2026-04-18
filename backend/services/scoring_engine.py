'''import re

# basic skill list (we will improve later)
SKILL_SET = [
    "python", "java", "c++", "sql", "machine learning",
    "data science", "flask", "django", "html", "css", "javascript"
]

def analyze_resume(text):
    text = text.lower()

    found_skills = []
    
    for skill in SKILL_SET:
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            found_skills.append(skill)

    # scoring logic
    score = int((len(found_skills) / len(SKILL_SET)) * 100)

    suggestions = []

    if score < 40:
        suggestions.append("Add more technical skills")
    if "python" not in found_skills:
        suggestions.append("Add Python experience")
    if "sql" not in found_skills:
        suggestions.append("Add database (SQL) knowledge")

    return {
        "score": score,
        "skills_found": found_skills,
        "suggestions": suggestions
    }'''

def calculate_score(text, skills_found):

    score = 0
    text = text.lower()

    # Skills score (40)
    required = ["python", "java", "c++", "html", "css", "javascript", "sql"]

    match = 0
    for s in required:
        if s in skills_found:
            match += 1

    score += (match / len(required)) * 40

    # Education (20)
    if "b.tech" in text or "bachelor" in text:
        score += 20

    # Projects (20)
    if "project" in text:
        score += 20

    # Keywords (20)
    keywords = ["developer", "engineer", "internship", "software"]

    kw = 0
    for k in keywords:
        if k in text:
            kw += 1

    score += (kw / len(keywords)) * 20

    return round(score, 2)