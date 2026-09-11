career_requirements = {
    "Data Scientist": {
        "python": 9,
        "sql": 8,
        "mathematics": 9,
        "statistics": 9,
        "machine_learning": 8,
        "data_visualization": 8
    },
    "Machine Learning Engineer": {
        "python": 10,
        "sql": 7,
        "mathematics": 9,
        "statistics": 8,
        "machine_learning": 10,
        "data_structures": 8
    },
    "Software Developer": {
        "python": 8,
        "sql": 7,
        "data_structures": 8,
        "problem_solving": 8,
        "communication": 7
    }
}


def find_skill_gaps(user_skills, career):
    required_skills = career_requirements.get(career)

    if required_skills is None:
        return {"error": "Career not found"}

    strong_skills = []
    skill_gaps = []

    for skill, required_level in required_skills.items():
        user_level = user_skills.get(skill, 0)

        if user_level >= required_level:
            strong_skills.append(skill)
        else:
            skill_gaps.append({
                "skill": skill,
                "current_level": user_level,
                "required_level": required_level,
                "needed": required_level - user_level
            })

    return {
        "career": career,
        "strong_skills": strong_skills,
        "skill_gaps": skill_gaps
    }


