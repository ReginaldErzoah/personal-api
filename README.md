# Personal API

A REST API built with **Python and FastAPI** to provide structured access to personal profile and professional skills information.

Personal API is a hands-on software engineering project focused on developing practical skills in REST API design, request handling, routing, data filtering, error handling, and application structure. It is being developed incrementally as part of a broader journey toward Data Engineering, MLOps, and reliable data systems.

## Overview

Personal API exposes profile information and a collection of professional skills through HTTP endpoints. Clients can retrieve profile data, list skills, filter skills by category, and look up an individual skill.

The project provides a practical environment for learning how to design and implement APIs before introducing more advanced capabilities such as persistent storage, automated testing, authentication, and containerisation.

## Current Features

- Built with FastAPI and Python.
- Retrieve API health information.
- Retrieve personal profile information.
- List available skills.
- Filter skills by category using query parameters.
- Retrieve skills belonging to a specific category through a dedicated route.
- Retrieve an individual skill by name.
- Return HTTP 404 errors when requested skills or categories are not found.
- Generate interactive API documentation through FastAPI.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and data handling |
| FastAPI | REST API development and request handling |
| Uvicorn | ASGI server used to run the application |
| Git and GitHub | Version control and source code management |

## API Endpoints

The following endpoints represent the current application interface.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Access the root endpoint |
| `GET` | `/health` | Check API health |
| `GET` | `/profile` | Retrieve profile information |
| `GET` | `/skills` | Retrieve all skills |
| `GET` | `/skills?category=programming` | Filter skills by category |
| `GET` | `/skills/category/{category_name}` | Retrieve skills belonging to a category |
| `GET` | `/skills/{skill_name}` | Retrieve a skill by name |

### Example Requests

Retrieve all skills:

```http
GET /skills
```

Filter skills by category:

```http
GET /skills?category=programming
```

Retrieve skills using the category route:

```http
GET /skills/category/data
```

Retrieve an individual skill:

```http
GET /skills/Python
```

The category and skill names must match the values supported by the current application. Matching behaviour depends on the implemented comparison logic.

### Error Handling

When a requested skill or category does not exist, the API returns an HTTP `404 Not Found` response.

FastAPI also provides request validation and interactive API documentation.

## Getting Started

### Prerequisites

Install the following software:

- Python 3.12 or a compatible supported version.
- Git.
- A terminal such as Git Bash, PowerShell, or a Linux shell.

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd personal-api
```

Replace `<your-repository-url>` with the HTTPS or SSH URL of your GitHub repository.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows Git Bash:

```bash
source .venv/Scripts/activate
```

On Linux or WSL Ubuntu:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

Install the packages declared by your project. If your repository uses a `pyproject.toml` with `uv`, use the project's configured dependency workflow. Otherwise, install the required dependencies using your chosen package manager.

For a basic installation:

```bash
python -m pip install fastapi "uvicorn[standard]"
```

### 4. Run the API

If the application entry point is `src/personal_api/main.py`, and the project is configured for imports from the `src` directory, run:

```bash
uvicorn personal_api.main:app --reload --app-dir src
```

The development server will normally be available at:

```text
http://127.0.0.1:8000
```

### 5. Explore the API

Open the interactive Swagger UI documentation:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

You can inspect available endpoints, supply parameters, send requests, and examine responses directly from your browser.

Alternative documentation is available at:

[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Structure

The current application entry point is located at `src/personal_api/main.py`.

```text
personal-api/
├── src/
│   └── personal_api/
│       └── main.py
├── .gitignore
├── pyproject.toml
└── README.md
```

This is a simplified representation. Keep only files and directories that actually exist in the repository when documenting the final project structure.

## Current Limitations

The current version is intentionally focused on foundational API development.

- Skills are stored in an in-memory Python collection.
- Data changes are not persisted to a database.
- The API currently focuses on retrieval operations rather than complete CRUD functionality.
- Authentication and authorization are not implemented.
- Automated test coverage and Docker-based deployment are not yet documented as completed capabilities.

Because the skills data is held in memory, changes made during application execution will not survive a process restart.

## Development Roadmap

Planned enhancements will be introduced as the project develops:

- [ ] Introduce structured request and response models using Pydantic.
- [ ] Improve input validation and error handling.
- [ ] Add automated unit and API tests using `pytest`.
- [ ] Implement create, update, and delete operations.
- [ ] Introduce persistent storage with SQLite or PostgreSQL.
- [ ] Separate routing, business logic, and data access into appropriate modules.
- [ ] Add configuration management and environment variables.
- [ ] Containerise the application with Docker.
- [ ] Add a Docker Compose workflow when supporting services are introduced.
- [ ] Automate quality checks and tests with GitHub Actions.
- [ ] Deploy the API and document its operational requirements.

These are planned enhancements, not claims about features already implemented.

## Learning Objectives

This project is designed to build practical understanding of:

- Python programming and application structure.
- REST principles and HTTP methods.
- FastAPI path operations and parameter handling.
- Query-based filtering and resource retrieval.
- HTTP status codes and exception handling.
- API documentation and manual endpoint testing.
- Testing, persistence, containerisation, and deployment as future engineering stages.

## Project Philosophy

The objective is not simply to make endpoints return responses. It is to understand why an API is designed a particular way, how requests move through the application, how errors should be handled, and how the software can become reliable and maintainable.

Each enhancement should introduce a clear engineering concept and be validated before additional complexity is added.

## Author

**Reginald Erzoah**

GitHub: [ReginaldErzoah](https://github.com/ReginaldErzoah)

Portfolio: [reginalderzoah.github.io](https://reginalderzoah.g
