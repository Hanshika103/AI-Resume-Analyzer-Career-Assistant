def extract_skills(text):

    skills_list = [
        "python", "java", "c++", "html", "css",
        "javascript", "sql", "flask", "django"
    ]

    found = []
    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found.append(skill)

    return found