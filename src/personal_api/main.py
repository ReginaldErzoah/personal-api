from datetime import date

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title = "Personal CV API",
    description = "A REST API providing structured information found on my professional CV.",
    version = "1.0.0"
)
