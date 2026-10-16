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