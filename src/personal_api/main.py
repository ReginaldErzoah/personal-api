
from fastapi import FastAPI, HTTPException

app = FastAPI()

SKILLS = [
    {"name": "Python", "category": "programming"},
    {"name": "SQL", "category": "data"},
    {"name": "FastAPI", "category": "programming"},
    {"name": "Power BI", "category": "data"},
    {"name": "Google Sheets", "category":"data" }
]


@app.get("/health")
def get_health():
    return {"status": "healthy"}


@app.get("/")
def read_root():
    return {"message": "Welcome to my Personal API!"}


@app.get("/profile")
def get_profile():
    return {
        "name": "Reginald",
        "profession": "Data Professional",
        "location": "Ghana",
    }


@app.get("/skills")
def get_skills(category: str | None = None):
    if category is None:
        return SKILLS

    matching_skills = [
        skill for skill in SKILLS
        if skill["category"].lower() == category.lower()
    ]

    return matching_skills


@app.get("/skills/category/{category_name}")
def get_category_name(category_name: str):
    matching_skills = [
        skill for skill in SKILLS
        if skill["category"].lower() == category_name.lower()
    ]

    if not matching_skills:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )

    return matching_skills


@app.get("/skills/{skill_name}")
def get_skill_name(skill_name: str):
    for skill in SKILLS:
        if skill["name"].lower() == skill_name.lower():
            return skill

    raise HTTPException(
        status_code=404,
        detail="Skill not found",
    )
