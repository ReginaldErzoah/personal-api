import os
from urllib.parse import quote

import gradio as gr
import requests


DEFAULT_API_URL = os.getenv(
    "PERSONAL_API_URL",
    "http://127.0.0.1:8000"
)

APP_TITLE = "Personal API"
APP_DESCRIPTION = """
Explore my profile professional profile, technical skills, projects 
and certifications through my Personal API.
"""