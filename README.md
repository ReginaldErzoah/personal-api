# Personal API

A personal professional profile platform built with **Python, FastAPI, and Gradio**, exposing my CV as structured, machine-readable data through a REST API and an interactive web interface.

Personal API represents my professional profile, technical skills, projects, education, work experience, and certifications through a documented HTTP interface.

Beyond its functionality, this project is a practical software engineering initiative through which I am developing skills in API development, frontend integration, software testing, containerisation, and deployment.

## Project Objectives

- Represent professional information through structured API resources.
- Build reliable, well-documented REST endpoints.
- Develop an interactive frontend that consumes the backend API.
- Apply software engineering practices for testing, maintainability, and code quality.
- Package the backend and frontend as independent Docker images.
- Publish container images to GitHub Container Registry (GHCR).
- Establish an automated testing and deployment workflow.

## Architecture

The application follows a two-component architecture.

| Component | Technology | Responsibility |
|---|---|---|
| Backend | FastAPI | Exposes professional information through REST API endpoints. |
| Frontend | Gradio | Provides an interactive interface for exploring professional information. |

The frontend communicates with the backend through HTTP requests.

The backend is responsible for retrieving and returning structured data, while the frontend presents that information to users.

The two applications are designed to be independently containerised and deployed.

## Current Features

### Backend

- Personal profile endpoint.
- Skills listing and individual skill lookup.
- Project listing and individual project lookup.
- Education information.
- Work experience information.
- Certifications listing and individual certification lookup.
- Health-check and welcome endpoints.
- HTTP error handling for applicable missing resources.
- Interactive API documentation powered by FastAPI.

### Frontend

- Interactive professional profile interface.
- Profile information retrieval.
- Technical skills exploration.
- Individual skill search.
- Project exploration and lookup.
- Certification exploration and lookup.
- Configurable backend API connection URL.
- API connection health check.
- Structured JSON response presentation.

## Technology Stack

| Category | Technology | Purpose |
|---|---|---|
| Programming Language | Python | Application development |
| Backend | FastAPI | REST API development |
| Frontend | Gradio | Interactive web interface |
| Data Validation | Pydantic | Data models and validation |
| HTTP Client | Requests | Frontend-to-backend communication |
| ASGI Server | Uvicorn / FastAPI CLI | Serving the backend application |
| Dependency Management | uv | Python project and dependency management |
| Testing | pytest | Automated application testing |
| Code Quality | Ruff | Linting and code quality |
| Version Control | Git | Source code version management |
| Source Hosting | GitHub | Repository hosting and collaboration |
| Containerisation | Docker | Packaging backend and frontend applications |
| Container Registry | GitHub Container Registry | Publishing and distributing Docker images |

## API Endpoints

The following table describes the main API resources. Consult the running application's Swagger documentation for the authoritative endpoint definitions and available parameters.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | API health information |
| GET | `/profile` | Retrieve professional profile |
| GET | `/skills` | List available skills |
| GET | `/skills/{skill_name}` | Retrieve an individual skill |
| GET | `/projects` | List available projects |
| GET | `/projects/by_id/{project_id}` | Retrieve a project by ID |
| GET | `/projects/by_name/{project_name}` | Retrieve a project by name |
| GET | `/education` | Retrieve education information |
| GET | `/experience` | Retrieve professional experience |
| GET | `/certifications` | List available certifications |
| GET | `/certifications/by_id/{certification_id}` | Retrieve a certification by ID |
| GET | `/certifications/{certification_name}` | Retrieve a certification by name |

## Getting Started

### Prerequisites

- Python 3.12 or a compatible version supported by the project.
- Git.
- uv.
- A terminal or command-line interface.

### 1. Clone the repository

```bash
git clone https://github.com/ReginaldErzoah/personal-api.git

cd personal-api
```

### 2. Install dependencies

```bash
uv sync
```

This creates or synchronises the project's virtual environment and installs its declared dependencies, including development dependencies.

### 3. Start the backend

```bash
uv run fastapi dev src/personal_api/main.py
```

The FastAPI development server will start locally.

The backend will be available at:

`http://127.0.0.1:8000`

### 4. Start the frontend

Open a second terminal in the project root and execute:

```bash
uv run python src/personal_api/frontend.py
```

The Gradio application will start and display its local web address in the terminal.

By default, the frontend connects to:

`http://127.0.0.1:8000`

Both applications must be running for the frontend to retrieve information from the backend.

### 5. Configure the backend URL

The frontend supports a configurable backend URL through the `PERSONAL_API_URL` environment variable.

For example, in Git Bash:

```bash
export PERSONAL_API_URL="http://127.0.0.1:8000"
```

This allows the frontend to communicate with a different backend address without changing the source code.

### 6. Explore the applications

**Backend documentation**

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

**Frontend**

Use the local Gradio URL printed in your terminal when the frontend starts.

## Project Structure

```text
personal-api/
│
├── src/
│   └── personal_api/
│       ├── __init__.py
│       ├── main.py
│       └── frontend.py
│
├── tests/
│   └── test_main.py
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
├── README.md
├── DEVELOPMENT_ROADMAP.md
└── LICENSE
```

The project uses a `src` layout to organise its Python application code into a package.

- `main.py` contains the FastAPI backend.
- `frontend.py` contains the Gradio frontend.
- `tests/` contains automated backend tests.
- `pyproject.toml` defines project metadata, dependencies, and configuration.
- `uv.lock` records the resolved dependency versions.

## Testing and Code Quality

The project uses pytest for automated testing and Ruff for code quality checks.

Run the test suite:

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov=personal_api
```

Run Ruff linting:

```bash
uv run ruff check .
```

## Containerisation and Deployment

The next stage of development is to package the backend and frontend into separate Docker images.

The intended container architecture is:

| Container Image | Application | Container Port |
|---|---|---|
| `personal-api-backend` | FastAPI | 8000 |
| `personal-api-frontend` | Gradio | 7860 |

The images will be published to GitHub Container Registry (GHCR).

Planned container registry references:

```text
ghcr.io/reginalderzoah/personal-api-backend:latest

ghcr.io/reginalderzoah/personal-api-frontend:latest
```

These are intended image names; the images will become available after successful builds and publication.

Future deployment work will include configuring communication between the containers, environment variables, and automated image publishing.

## Current Limitations

- Professional information is not yet backed by persistent database storage.
- The API primarily supports read operations.
- The frontend depends on the backend being available.
- Production containerisation and deployment are still being implemented.
- Automated CI/CD workflows are part of the planned development process.
