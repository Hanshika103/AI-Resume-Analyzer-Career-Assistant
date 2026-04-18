def recommend_job(skills):
    skills = [s.lower() for s in skills]

    if "python" in skills:
        return "Python Developer"
    elif "java" in skills:
        return "Java Developer"
    elif "javascript" in skills:
        return "Frontend Developer"
    elif "sql" in skills:
        return "Data Analyst"
    else:
        return "Software Developer"