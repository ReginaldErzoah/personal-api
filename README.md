# Personal API

A personal professional profile platform built with **Python, FastAPI, and Gradio**, exposing my CV as structured, machine-readable data through a REST API and an interactive web interface.

Personal API represents my professional profile, technical skills, projects, education, work experience, and certifications through a documented HTTP interface.

Beyond its functionality, this project is a practical software engineering initiative through which I am developing skills in API development, frontend integration, software testing, containerization, application architecture, and deployment.

## Project Objectives

- Represent professional information through structured API resources.
- Build reliable, well-documented REST API endpoints.
- Develop an interactive frontend that consumes the backend API.
- Apply software engineering practices for testing, maintainability, and code quality.
- Package the backend and frontend as independent Docker images.
- Orchestrate multiple application services using Docker Compose.
- Publish and distribute container images through GitHub Container Registry (GHCR).
- Establish an automated testing and deployment workflow.

## Architecture

The application follows a two-component architecture consisting of an independent backend and frontend.

| Component | Technology | Responsibility |
|---|---|---|
| Backend | FastAPI | Exposes professional information through REST API endpoints. |
| Frontend | Gradio | Provides an interactive interface for exploring professional information. |
| Containerization | Docker | Packages the backend and frontend independently. |
| Orchestration | Docker Compose | Builds, configures, connects, and manages both application services. |
| Container Registry | GHCR | Stores and distributes published Docker images. |

The frontend communicates with the backend through HTTP requests.

The backend is responsible for retrieving and returning structured data, while the frontend presents that information to users.

Both applications are independently containerized and communicate through a Docker Compose network. The frontend uses the backend service name to access the API internally.

### Application Architecture

```text
                 User
                  |
                  v
          Gradio Frontend
             Port 7860
                  |
                  | HTTP
                  |
          Docker Network
                  |
                  v
           FastAPI Backend
              Port 8000
                  |
                  v
          Structured API Data
```

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

### Containerization and Deployment

- Independent backend and frontend Dockerfiles.
- Separate Docker images for each application component.
- Docker Compose service orchestration.
- Container-to-container communication through an internal Docker network.
- Environment-based backend URL configuration.
- Published Docker images on GitHub Container Registry.
- Versioned container images (`1.0.0`).

## Technology Stack

| Category | Technology | Purpose |
|---|---|---|
| Programming Language | Python | Application development |
| Backend | FastAPI | REST API development |
| Frontend | Gradio | Interactive web interface |
| Data Validation | Pydantic | Data models and validation |
| HTTP Client | Requests | Frontend-to-backend communication |
| ASGI Server | FastAPI CLI / Uvicorn | Serving the backend application |
| Dependency Management | uv | Python project and dependency management |
| Testing | pytest | Automated application testing |
| Code Quality | Ruff | Linting and code quality |
| Version Control | Git | Source code version management |
| Source Hosting | GitHub | Repository hosting and collaboration |
| Containerization | Docker | Packaging backend and frontend applications |
| Orchestration | Docker Compose | Managing multiple application containers |
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
- Docker Desktop with Docker Compose.
- A terminal or command-line interface.

### Option 1: Run Locally Using Python

#### 1. Clone the repository

```bash
git clone https://github.com/ReginaldErzoah/personal-api.git

cd personal-api
```

#### 2. Install dependencies

```bash
uv sync
```

This creates or synchronizes the project's virtual environment and installs its declared dependencies, including development dependencies.

#### 3. Start the backend

```bash
uv run fastapi dev src/personal_api/main.py
```

The backend will be available at:

`http://127.0.0.1:8000`

#### 4. Start the frontend

Open a second terminal in the project root and execute:

```bash
uv run python -m personal_api.frontend
```

The Gradio application will start and display its local web address in the terminal.

By default, the frontend connects to:

`http://127.0.0.1:8000`

Both applications must be running for the frontend to retrieve information from the backend.

#### 5. Configure the backend URL

The frontend supports a configurable backend URL through the `PERSONAL_API_URL` environment variable.

For example, in Git Bash:

```bash
export PERSONAL_API_URL="http://127.0.0.1:8000"
```

This allows the frontend to communicate with a different backend address without modifying the source code.

### Option 2: Run Using Docker Compose

The recommended containerized execution method is Docker Compose.

The project includes separate Dockerfiles for the backend and frontend, while `compose.yaml` defines how both services are built and executed.

#### 1. Clone the repository

```bash
git clone https://github.com/ReginaldErzoah/personal-api.git

cd personal-api
```

#### 2. Build and start the application

```bash
docker compose up --build -d
```

This command:

- Builds the backend Docker image.
- Builds the frontend Docker image.
- Creates the application containers.
- Configures the internal Docker network.
- Starts both services in the background.

#### 3. Verify running containers

```bash
docker compose ps
```

This displays the status of the backend and frontend containers.

#### 4. Access the applications

| Application | URL |
|---|---|
| Gradio Frontend | http://localhost:7860 |
| FastAPI Backend | http://localhost:8000 |
| Swagger Documentation | http://localhost:8000/docs |
| ReDoc Documentation | http://localhost:8000/redoc |
| Backend Health Check | http://localhost:8000/health |

#### 5. View application logs

View logs for both services:

```bash
docker compose logs
```

Follow logs continuously:

```bash
docker compose logs -f
```

View logs for an individual service:

```bash
docker compose logs backend
```

```bash
docker compose logs frontend
```

#### 6. Stop the application

```bash
docker compose down
```

This stops and removes the Compose containers and network. It does not delete the published images.

## Docker Images and GitHub Container Registry

The backend and frontend are packaged as separate Docker images and published to GitHub Container Registry.

### Published Images

| Component | GHCR Image | Version | Container Port |
|---|---|---|---|
| Backend | `ghcr.io/reginalderzoah/personal-api-backend` | `1.0.0` | 8000 |
| Frontend | `ghcr.io/reginalderzoah/personal-api-frontend` | `1.0.0` | 7860 |

### Pulling Published Images

The published images can be retrieved using:

```bash
docker pull ghcr.io/reginalderzoah/personal-api-backend:1.0.0
```

```bash
docker pull ghcr.io/reginalderzoah/personal-api-frontend:1.0.0
```

Package access depends on the visibility and permissions configured in GitHub.

### Image Publishing Workflow

The current image publishing process involves:

1. Developing and testing the application.
2. Building the backend and frontend Docker images.
3. Assigning version tags to the images.
4. Authenticating Docker with GitHub Container Registry.
5. Pushing the images to GHCR.
6. Associating the published packages with the GitHub repository.

The published images are versioned independently from the application source code.

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
├── Dockerfile.backend
├── Dockerfile.frontend
├── compose.yaml
├── .dockerignore
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
├── README.md
├── DEVELOPMENT_ROADMAP.md
└── LICENSE
```

### Key Files

| File | Responsibility |
|---|---|
| `main.py` | Contains the FastAPI backend. |
| `frontend.py` | Contains the Gradio frontend. |
| `tests/` | Contains automated backend tests. |
| `Dockerfile.backend` | Defines how the backend image is built. |
| `Dockerfile.frontend` | Defines how the frontend image is built. |
| `compose.yaml` | Defines and manages the backend and frontend services. |
| `.dockerignore` | Excludes unnecessary files from Docker build contexts. |
| `pyproject.toml` | Defines project metadata, dependencies, and configuration. |
| `uv.lock` | Records resolved dependency versions. |
| `DEVELOPMENT

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

## Current Limitations

- Professional information is not yet backed by persistent database storage.
- The API primarily supports read operations.
- The frontend depends on the backend being available.
- Automated CI/CD workflows have not yet been fully implemented.
- Production deployment, monitoring, and operational observability remain areas for further development.

## Future Development

The next stages of development will focus on:

- Introducing persistent database storage.
- Improving API architecture and data management.
- Expanding automated testing and test coverage.
- Implementing CI/CD using GitHub Actions.
- Automating Docker image builds and publication.
- Deploying the application to a cloud environment.
- Introducing application monitoring and operational logging.
- Improving security and production configuration.

## Learning Outcomes

Personal API serves as a practical engineering project for developing experience in:

- REST API design and development.
- Python application packaging and dependency management.
- Backend and frontend integration.
- Data validation and API contracts.
- Automated testing and code quality.
- Docker image creation and optimization.
- Container networking and orchestration.
- Docker Compose.
- Container registry management and image distribution.
- Application deployment practices.
