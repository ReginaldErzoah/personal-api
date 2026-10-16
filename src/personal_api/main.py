from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def get_health():
    return {
        "status" : "healthy"
    }

@app.get("/")
def read_root():
    return {"message": "Welcome to my Personal API!"}

@app.get("/profile")
def get_profile():
    return {
        "name" : "Reginald",
        "profession" : "Data Professional",
        "location" : "Ghana"
    }

@app.get("/skills")
def get_skills():
    return {
        "skills" : ["Python","SQL", "FastAPI"]
    }

@app.get("/skills/{skill_name}")
def get_skill_name(skill_name):    
    skills = ["Python","SQL"]

    for skill in skills:
        if skill == skill_name:
            return skill