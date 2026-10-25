from datetime import date

from fastapi import FastAPI
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


class Certifications(BaseModel):
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
        description = 
        """
        A REST API for exposing structured professional 
        profile, skills, projects, experience, education, 
        and certification information.
        """,
        technologies = ["Python", "FastAPI", "Pydantic", "Docker"],
        status = "in progress",
        repo_url = "https://github.com/ReginaldErzoah/personal-api"
    ),
]


CERTIFICATIONS = [
    Certifications(
        id = 1,
        name = "Machine Learning Specialization",
        issuing_organization = "Standford Online & DeepLearning.AI",
        issue_date = date(2026,6,20),
        credential_url = "https://www.coursera.org/account/accomplishments/specialization/NZFV7TO6HEDH"
    ),

    Certifications(
        id = 2,
        name = "Product Analytics Micro-Certification",
        issuing_organization = "Product School",
        issue_date = date(2025,7,31)
    ),

   Certifications(
       id = 3,
       name = "Data Management Professional Certficate",
       issuing_organization = "IBM",
       issue_date = date (2025,2,9),
       credential_url = "https://www.coursera.org/account/accomplishments/professional-cert/OH2YCGHZE01U"
   ),

   Certifications(
       id = 4,
       name = "Database Systems Specialization",
       issuing_organization = "Universidad Nacional Autónoma de México",
       issue_date = date(2025,2,1)
   ),    
]


def find_by_id(items:list, item_id:int, resource_name:str):