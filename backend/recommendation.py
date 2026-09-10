careers = {
    "Data Scientist": {
        "python": 9,
        "sql": 8,
        "mathematics": 9,
        "statistics": 9,
        "machine_learning": 8,
        "communication": 7
    },
    "Machine Learning Engineer": {
        "python": 10,
        "sql": 7,
        "mathematics": 9,
        "statistics": 8,
        "machine_learning": 10,
        "communication": 6
    },
    "Software Developer": {
        "python": 8,
        "sql": 7,
        "mathematics": 6,
        "statistics": 5,
        "machine_learning": 5,
        "communication": 7
    },
    "Data Analyst": {
        "python": 7,
        "sql": 9,
        "mathematics": 7,
        "statistics": 8,
        "machine_learning": 5,
        "communication": 8
    },
    "Cybersecurity Analyst": {
        "python": 7,
        "sql": 6,
        "mathematics": 7,
        "statistics": 6,
        "machine_learning": 6,
        "communication": 7
    }
}


def calculate_match(user_skills, career_skills):
    total = 0
    count = 0

    for skill, required_level in career_skills.items():
        user_level = user_skills.get(skill, 0)
        match = min(user_level / required_level, 1)
        total += match
        count += 1

    return round((total / count) * 100, 2)


def recommend_careers(user_skills):
    results = []

    for career, required_skills in careers.items():
        score = calculate_match(user_skills, required_skills)

        results.append({
            "career": career,
            "match": score
        })

    results.sort(key=lambda x: x["match"], reverse=True)

    return results


user = {
    "python": 8,
    "sql": 6,
    "mathematics": 9,
    "statistics": 7,
    "machine_learning": 6,
    "communication": 7
}


recommendations = recommend_careers(user)

print("\nCareer Recommendations\n")

for result in recommendations:
    print(f"{result['career']}: {result['match']}%")