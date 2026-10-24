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

class Cerfiticatons(BaseModel):
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
