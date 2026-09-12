from backend.recommendation import recommend_careers
from backend.skill_gap import find_skill_gaps
from backend.roadmap import generate_roadmap


def get_user_skills():
    print("\n========== AI CAREER GUIDANCE SYSTEM ==========\n")

    user_input = input("Enter your skills separated by commas: ")

    user_skills = [
        skill.strip().lower()
        for skill in user_input.split(",")
        if skill.strip()
    ]

    return user_skills


def display_careers(careers):
    print("\n========== CAREER RECOMMENDATIONS ==========\n")

    if not careers:
        print("No suitable careers found.")
        return None

    for index, career in enumerate(careers, start=1):
        print(
            f"{index}. {career['career']} - "
            f"{career['match']}% match"
        )

    while True:
        try:
            choice = int(input("\nSelect a career number: "))

            if 1 <= choice <= len(careers):
                return careers[choice - 1]["career"]

            print("Please select a valid career number.")

        except ValueError:
            print("Please enter a valid number.")


def display_skill_gap(user_skills, selected_career):
    print("\n========== SKILL-GAP ANALYSIS ==========\n")

    result = find_skill_gaps(
        user_skills,
        selected_career
    )

    if "error" in result:
        print(result["error"])
        return None

    print("Strong Skills:")

    strong_skills = result.get("strong_skills", [])

    if strong_skills:
        for skill in strong_skills:
            print(f"- {skill}")
    else:
        print("- No strong skills identified")

    print("\nMissing Skills:")

    skill_gaps = result.get("skill_gaps", [])

    if not skill_gaps:
        print("- No major skill gaps found")
    else:
        for gap in skill_gaps:
            skill_name = gap["skill"].replace("_", " ").title()

            print(
                f"- {skill_name} "
                f"(Current: {gap['current_level']}, "
                f"Required: {gap['required_level']})"
            )

    return skill_gaps


def display_roadmap(selected_career, skill_gaps):
    print("\n========== PERSONALIZED LEARNING ROADMAP ==========\n")

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

        for skill in stage["skills"]:
            print(f"- {skill}")

        print("\nLearning Tasks:")

        for task in stage["tasks"]:
            print(f"- {task}")

        print(f"\nPractical Project: {stage['project']}")

    print("\nPossible Entry-Level Job Roles:")

    for role in result["job_roles"]:
        print(f"- {role}")


def main():
    user_skills = get_user_skills()

    if not user_skills:
        print("\nPlease enter at least one skill.")
        return

    careers = recommend_careers(user_skills)

    selected_career = display_careers(careers)

    if selected_career is None:
        return

    skill_gaps = display_skill_gap(
        user_skills,
        selected_career
    )

    if skill_gaps is None:
        return

    display_roadmap(
        selected_career,
        skill_gaps
    )

    print("\n==============================================")
    print("Career guidance process completed successfully.")
    print("==============================================")


if __name__ == "__main__":
    main()