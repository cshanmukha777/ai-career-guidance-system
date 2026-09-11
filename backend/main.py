from recommendation import recommend_careers
from skill_gap import find_skill_gaps
from roadmap import generate_roadmap


def display_recommendations(user_skills):
    recommendations = recommend_careers(user_skills)

    print("\nCareer Recommendations\n")

    for index, result in enumerate(recommendations[:3], start=1):
        print(f"{index}. {result['career']} - {result['match']}%")


def get_skill_gaps(user_skills, career):
    result = find_skill_gaps(user_skills, career)

    if "error" in result:
        print(result["error"])
        return []

    print("\nSkill Gap Analysis\n")

    print("Strong Skills:")
    for skill in result["strong_skills"]:
        print("-", skill)

    print("\nMissing Skills:")
    for gap in result["skill_gaps"]:
        print(
            f"- {gap['skill']} "
            f"(Current: {gap['current_level']}/10, "
            f"Required: {gap['required_level']}/10)"
        )

    return result["skill_gaps"]


def display_roadmap(career, skill_gaps):
    result = generate_roadmap(career, skill_gaps)

    if "error" in result:
        print(result["error"])
        return

    print("\nPersonalized Learning Roadmap\n")

    for item in result["roadmap"]:
        print(f"\nSkill: {item['skill']}")

        for step_number, step in enumerate(
            item["learning_steps"],
            start=1
        ):
            print(f"{step_number}. {step}")


def main():
    user_skills = {
        "python": 8,
        "sql": 6,
        "mathematics": 9,
        "statistics": 6,
        "machine_learning": 5,
        "data_visualization": 3,
        "communication": 7
    }

    display_recommendations(user_skills)

    selected_career = "Data Scientist"

    skill_gaps = get_skill_gaps(
        user_skills,
        selected_career
    )

    display_roadmap(
        selected_career,
        skill_gaps
    )


if __name__ == "__main__":
    main()