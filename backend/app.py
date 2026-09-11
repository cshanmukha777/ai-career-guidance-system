from fastapi import FastAPI
from pydantic import BaseModel

from backend.recommendation import recommend_careers
from backend.skill_gap import find_skill_gaps
from backend.roadmap import generate_roadmap

app = FastAPI(title="AI Career Guidance System")


class UserSkills(BaseModel):
    skills: dict


class CareerRequest(BaseModel):
    skills: dict
    career: str


@app.get("/")
def home():
    return {
        "message": "AI Career Guidance System API is running"
    }


@app.post("/recommend")
def get_recommendations(user: UserSkills):
    return {
        "recommendations": recommend_careers(user.skills)
    }


@app.post("/skill-gap")
def get_skill_gap(user: CareerRequest):
    return find_skill_gaps(user.skills, user.career)


@app.post("/roadmap")
def get_roadmap(user: CareerRequest):
    gap_result = find_skill_gaps(user.skills, user.career)

    if "error" in gap_result:
        return gap_result

    return generate_roadmap(
        user.career,
        gap_result["skill_gaps"]
    )