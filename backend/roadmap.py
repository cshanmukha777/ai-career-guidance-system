career_roadmaps = {
    "Data Scientist": {
        "sql": [
            "Learn SQL basics",
            "Practice SELECT, WHERE and JOIN",
            "Work with GROUP BY and subqueries"
        ],
        "statistics": [
            "Learn mean, median and standard deviation",
            "Study probability",
            "Learn correlation and hypothesis testing"
        ],
        "machine_learning": [
            "Learn supervised and unsupervised learning",
            "Study regression and classification",
            "Build a machine learning project"
        ],
        "data_visualization": [
            "Learn Matplotlib",
            "Learn Seaborn",
            "Create dashboards using Power BI"
        ],
        "python": [
            "Practice Python functions",
            "Learn NumPy and Pandas",
            "Work with real datasets"
        ]
    },
    "Machine Learning Engineer": {
        "python": [
            "Practice advanced Python",
            "Learn NumPy and Pandas",
            "Learn object-oriented programming"
        ],
        "machine_learning": [
            "Learn regression and classification",
            "Study model evaluation",
            "Build machine learning projects"
        ],
        "data_structures": [
            "Learn arrays and linked lists",
            "Learn stacks, queues and trees",
            "Practice coding problems"
        ],
        "statistics": [
            "Learn probability",
            "Study statistics",
            "Understand model performance metrics"
        ]
    },
    "Software Developer": {
        "python": [
            "Learn Python basics",
            "Practice functions and modules",
            "Build Python projects"
        ],
        "data_structures": [
            "Learn arrays and linked lists",
            "Learn stacks, queues and trees",
            "Practice sorting and searching"
        ],
        "problem_solving": [
            "Practice basic programming problems",
            "Learn recursion",
            "Solve coding challenges"
        ],
        "sql": [
            "Learn SQL basics",
            "Practice database queries",
            "Learn joins and aggregation"
        ]
    }
}


def generate_roadmap(career, skill_gaps):
    career_plan = career_roadmaps.get(career)

    if career_plan is None:
        return {"error": "Roadmap not found"}

    roadmap = []

    for gap in skill_gaps:
        skill = gap["skill"]

        if skill in career_plan:
            roadmap.append({
                "skill": skill,
                "current_level": gap["current_level"],
                "required_level": gap["required_level"],
                "learning_steps": career_plan[skill]
            })

    return {
        "career": career,
        "roadmap": roadmap
    }


skill_gaps = [
    {
        "skill": "sql",
        "current_level": 6,
        "required_level": 8
    },
    {
        "skill": "statistics",
        "current_level": 6,
        "required_level": 9
    },
    {
        "skill": "machine_learning",
        "current_level": 5,
        "required_level": 8
    },
    {
        "skill": "data_visualization",
        "current_level": 3,
        "required_level": 8
    }
]

career = "Data Scientist"

result = generate_roadmap(career, skill_gaps)

print("\nPersonalized Career Roadmap\n")
print("Career:", result["career"])

for item in result["roadmap"]:
    print("\nSkill:", item["skill"])
    print(
        "Current Level:",
        item["current_level"],
        "/ Required Level:",
        item["required_level"]
    )

    print("Learning Steps:")

    for step in item["learning_steps"]:
        print("-", step)