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
    portfolio_url : str
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

class Cerfiticatons(BaseModel):
    id : int
    name : str
    issuing_organization : str
    issue_date : date | None = None
    credential_url : str 
