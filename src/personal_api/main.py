from datetime import date

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title = "Personal CV API",
    description = "A REST API providing structured information found on my professional CV.",
    version = "1.0.0"
)


class Profile(BaseModel):
    name : str
    profession : str
    location : str
    summary : str
    portfolio_url : str | None = None
    github_url : str
    linkedin_url : str 


class Skill(BaseModel):
    name : str
    category : str
    level : str | None = None


class Project(BaseModel):
    id : int
    name : str
    description : str
    technologies : list[str]
    status : str | None = None
    repo_url : str | None = None


class Certification(BaseModel):
    id : int
    name : str
    issuing_organization : str
    issue_date : date | None = None
    credential_url : str | None = None


PROFILE = Profile(
    name = "Reginald Erzoah",
    profession = "Data Professional",
    location = "Ghana",
    summary = "A data professional helping build trustworthy & reliable data systems.",
    portfolio_url = "https://reginalderzoah.github.io",
    github_url = "https://github.com/ReginaldErzoah",
    linkedin_url = "https://www.linkedin.com/in/reginald-erzoah"
)


SKILLS = [
    Skill(name = "Python", category = "programming"),
    Skill(name =  "FastAPI", category = "programming"),
    Skill(name = "git", category = "programming"),
    Skill(name = "SQL", category = "data"),
    Skill(name = "Power BI", category = "data"),
    Skill(name = "Google Sheets", category = "data"),
]


PROJECTS = [
    Project(
        id = 1,
        name = "Personal API",
        description =
        "A REST API for exposing structured professional profile, skills, projects, experience, education, and certification information.",
        technologies = ["Python", "FastAPI", "Pydantic", "Docker"],
        status = "in progress",
        repo_url = "https://github.com/ReginaldErzoah/personal-api"
    ),
]


CERTIFICATIONS = [
    Certification(
        id = 1,
        name = "Machine Learning Specialization",
        issuing_organization = "Stanford Online & DeepLearning.AI",
        issue_date = date(2026,6,20),
        credential_url = "https://www.coursera.org/account/accomplishments/specialization/NZFV7TO6HEDH"
    ),

    Certification(
        id = 2,
        name = "Product Analytics Micro-Certification",
        issuing_organization = "Product School",
        issue_date = date(2025,7,31)
    ),

   Certification(
       id = 3,
       name = "Data Management Professional Certficate",
       issuing_organization = "IBM",
       issue_date = date (2025,2,9),
       credential_url = "https://www.coursera.org/account/accomplishments/professional-cert/OH2YCGHZE01U"
   ),

   Certification(
       id = 4,
       name = "Database Systems Specialization",
       issuing_organization = "Universidad Nacional Autónoma de México",
       issue_date = date(2025,2,1)
   ),    
]


def normalize_text(value:str) -> str:
    return value.strip().casefold()


def find_by_id(items:list, item_id:int, resource_name:str):
    for item in items:
        if item.id == item_id:
            return item

    raise HTTPException(
        status_code = 404,
        detail = f"{resource_name} with ID {item_id} not found."
    )


def find_by_name(items:list, item_name:str, resource_name:str):
    normalized_name = normalize_text(item_name)
    for item in items:
        if normalize_text(item.name) == normalized_name:
            return item

    raise HTTPException(
        status_code = 404,
        detail = f"{resource_name} named {item_name} not found"
    )


@app.get("/", tags=["General"])
def read_root():
    return {"message" : "Welcome to my Personal CV API"}


@app.get("/health", tags=["General"])
def get_health():
    return {"status" : "healthy"}


@app.get("/profile", response_model=Profile, tags=["Profile"])
def get_profile():
    return PROFILE

@app.get("/skills", response_model=list[Skill], tags=["Skills"])
def get_skills():
    return SKILLS


@app.get("/skills/{skill_name}", response_model=Skill, tags=["Skills"])
def get_skill_by_name(skill_name:str):
    return find_by_name(SKILLS, skill_name, "Skill")


@app.get("/projects", response_model = list[Project], tags=["Projects"])
def get_projects():
    return PROJECTS


@app.get("/Profile/{project_name}", response_model=Project, tags =["Projects"])
def get_projects_by_name(project_name : str):
    return find_by_name(PROJECTS, project_name, "Project")


@app.get("Projects/{project_id}", response_model=Project, tags=["Projects"])
def get_projects_by_id(project_id:int):
    