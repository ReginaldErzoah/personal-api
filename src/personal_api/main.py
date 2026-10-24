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