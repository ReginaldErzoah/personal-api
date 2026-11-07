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

    except requests.exceptions.RequestException as error:
        return {
            "error": "An unexpected request error occurred.",
            "details": str(error)
        }


def check_api_health(api_url):
    return make_request(api_url,"/health")


def get_profile(api_url):
    return make_request(api_url,"/profile")


def get_skills(api_url):
    return make_request(api_url,"/skills")


def get_skill_by_name(api_url, skill_name):

    if not skill_name or not skill_name.strip():
        return {"error": "Enter a skill name."}

    endpoint = f"/skills/{quote(skill_name.strip(),safe='')}"

    return make_request(api_url,endpoint)


def get_projects(api_url):
    return make_request(api_url,"/projects")


def get_project_by_id(api_url, project_id):

    if not project_id or not str(project_id).strip():
        return {"error": "Enter a project ID."}

    endpoint = f"/projects/by_id/{quote(str(project_id).strip(),safe='')}"

    return make_request(api_url,endpoint)


def get_project_by_name(api_url,project_name):

    if not project_name or not project_name.strip():
        return {"error": "Enter project name."}

    endpoint = f"/projects/by_name/{quote(str(project_name).strip(),safe='')}"

    return make_request(api_url,endpoint)


def get_experience(api_url):
    return make_request(api_url, "/experience")


def get_education(api_url):
    return make_request(api_url, "/education")


def get_certifications(api_url):
    return make_request(api_url, "/certifications")


def get_certification_by_id(api_url, certification_id):

    if not certification_id or not str(certification_id).strip():
        return {"error": "Enter a certification ID."}

    endpoint = (
        f"/certifications/by_id/"
        f"{quote(str(certification_id).strip(), safe='')}"
    )

    return make_request(api_url, endpoint)


def get_certification_by_name(api_url, certification_name):

    if not certification_name or not certification_name.strip():
        return {"error": "Please enter a certification name."}

    endpoint = (
        f"/certifications/"
        f"{quote(certification_name.strip(), safe='')}"
    )

    return make_request(api_url, endpoint)


with gr.Blocks(title=APP_TITLE) as app:

    gr.Markdown(
        f"""
        # {APP_TITLE}

        {APP_DESCRIPTION}
        """
    )


    with gr.Accordion("API Connection Settings", open=False):

        api_url = gr.Textbox(
            label="FastAPI Base URL",
            value=DEFAULT_API_URL,
            placeholder="http://127.0.0.1:8000"
        )

        health_button = gr.Button("Check API Connection")

        health_output = gr.JSON(
            label="API Health Status"
        )

        health_button.click(
            fn=check_api_health,
            inputs=[api_url],
            outputs=[health_output]
        )


    with gr.Tab("Profile"):

        gr.Markdown("## Professional Profile")

        profile_button = gr.Button(
            "Load My Profile",
            variant="primary"
        )

        profile_output = gr.JSON(
            label="Profile Information"
        )

        profile_button.click(
            fn=get_profile,
            inputs=[api_url],
            outputs=[profile_output]
        )