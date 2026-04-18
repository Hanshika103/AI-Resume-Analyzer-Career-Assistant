def generate_feedback(text, skills):

    feedback = {
        "weakness": [],
        "improvements": [],
        "strengths": [],
        "suggestions": []
    }

    text_lower = text.lower()

    if "project" in text_lower and "impact" not in text_lower:
        feedback["weakness"].append("Projects lack measurable impact")

    if "flask" not in text_lower:
        feedback["improvements"].append("Add Flask/Django backend framework")

    if len(skills) < 5:
        feedback["weakness"].append("Too few technical skills listed")

    if "python" in skills:
        feedback["strengths"].append("Strong Python knowledge")

    feedback["suggestions"].append("Add GitHub links")
    feedback["suggestions"].append("Use measurable achievements")

    return feedback