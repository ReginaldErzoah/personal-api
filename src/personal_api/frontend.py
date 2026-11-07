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

def make_request(api_url: str, endpoint: str):

    api_url = api_url.strip().rstrip("/")

    if not api_url:
        return {"error": "Provide a valid API URL."}

    url = f"{api_url}/{endpoint.lstrip("/")}"

    try:
        response = requests.get(url,timeout=15)

        response.raise_for_status()

        try:
            response.json()

        except requests.exceptions.JSONDecodeError:
            return {"response": response.text}

    except requests.exceptions.ConnectionError:
        return {"error": "Couldn't connect to the API",
                "details": "Check if FastAPI application is running."
                "Make sure API url is also valid."}

    except requests.exceptions.Timeout:
        return {"error": "The API request timed out"}

    except requests.exceptions.HTTPError:
        try:
            error_details = response.json()
        except requests.exceptions.JSONDecodeError:
            error_details = response.text

        return {
            "error": f"API request failed with status: {response.status_code}.",
            "details": error_details
        }