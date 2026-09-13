from backend.recommendation import recommend_careers
from backend.skill_gap import find_skill_gaps
from backend.roadmap import generate_roadmap


def get_skill_level(skill):
    while True:
        try:
            value = int(
                input(
                    f"Enter your {skill} skill level (0-10): "
                )
            )

            if 0 <= value <= 10:
                return value

            print("Enter a value between 0 and 10.")

        except ValueError:
            print("Please enter a valid number.")


def display_recommendations(user_skills):
    recommendations = recommend_careers(user_skills)

    print("\nCareer Recommendations\n")

    for index, result in enumerate(
        recommendations[:3],
        start=1
    ):
        print(
            f"{index}. "
            f"{result['career']} - "
            f"{result['match']}%"
        )

    return recommendations[:3]


def get_skill_gaps(user_skills, career):
    result = find_skill_gaps(
        career,
        user_skills
    )

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
            f"Required: {gap['required_level']}/10, "
            f"Needed: {gap['needed']})"
        )

    return result["skill_gaps"]


def display_roadmap(selected_career, skill_gaps):
    print(
        "\n========== "
        "PERSONALIZED LEARNING ROADMAP "
        "==========\n"
    )

    result = generate_roadmap(
        selected_career,
        skill_gaps
    )

    if "error" in result:
        print(result["error"])
        return

    print(f"Career Goal: {result['career']}")
    print(f"Estimated Duration: {result['duration']}")

    print("\nLearning Stages:")

    for stage in result["stages"]:
        print(f"\n{stage['stage']}")

        print("\nSkills to Learn:")

        for skill in stage.get("skills", []):
            print(f"- {skill}")

        print("\nLearning Tasks:")

        for task in stage.get("tasks", []):
            print(f"- {task}")

        print(
            f"\nPractical Project: "
            f"{stage.get('project', 'No project specified')}"
        )

    print("\nPossible Entry-Level Job Roles:")

    for role in result["job_roles"]:
        print(f"- {role}")


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

    recommendations = display_recommendations(
        user_skills
    )

    print("\nChoose a career for detailed analysis:")

    for index, result in enumerate(
        recommendations,
        start=1
    ):
        print(f"{index}. {result['career']}")

    while True:
        try:
            choice = int(
                input("\nEnter your choice: ")
            )

            if 1 <= choice <= len(recommendations):
                selected_career = (
                    recommendations[choice - 1]["career"]
                )
                break

            print("Choose a valid career number.")

        except ValueError:
            print("Please enter a valid number.")

    print(
        f"\nSelected Career: "
        f"{selected_career}"
    )

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