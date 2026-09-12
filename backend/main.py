from backend.recommendation import recommend_careers
from backend.skill_gap import find_skill_gaps
from backend.roadmap import generate_roadmap

def get_skill_level(skill):
    while True:
        try:
            value = int(input(f"Enter your {skill} skill level (0-10): "))

            if 0 <= value <= 10:
                return value

            print("Enter a value between 0 and 10.")

        except ValueError:
            print("Please enter a valid number.")


def display_recommendations(user_skills):
    recommendations = recommend_careers(user_skills)

    print("\nCareer Recommendations\n")

    for index, result in enumerate(recommendations[:3], start=1):
        print(f"{index}. {result['career']} - {result['match']}%")

    return recommendations[:3]


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
    print("\n===== AI CAREER GUIDANCE SYSTEM =====\n")

    skills = [
        "python",
        "sql",
        "mathematics",
        "statistics",
        "machine_learning",
        "data_visualization",
        "communication"
    ]

    user_skills = {}

    for skill in skills:
        user_skills[skill] = get_skill_level(skill)

    print("\nAnalyzing your skills...")

    recommendations = display_recommendations(user_skills)

    print("\nChoose a career for detailed analysis:")

    for index, result in enumerate(recommendations, start=1):
        print(f"{index}. {result['career']}")

    while True:
        try:
            choice = int(input("\nEnter your choice: "))

            if 1 <= choice <= len(recommendations):
                selected_career = recommendations[choice - 1]["career"]
                break

            print("Choose a valid career number.")

        except ValueError:
            print("Please enter a valid number.")

    print(f"\nSelected Career: {selected_career}")

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