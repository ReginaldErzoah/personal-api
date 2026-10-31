# Personal API

A REST API built with **Python and FastAPI** to expose my professional CV as structured, machine-readable data.

Personal API represents my professional profile, technical skills, projects, education, and experience through a documented HTTP interface. It is also a practical software engineering project through which I am developing skills in API design, testing, containerisation, and deployment.

## Project Objectives

- Represent professional information through structured API resources.
- Build reliable and well-documented REST endpoints.
- Apply software engineering practices for testing, maintainability, and code quality.
- Package the application using Docker.
- Establish an automated testing and deployment workflow.

## Current Features

- Personal profile endpoint.
- Skills listing and category-based filtering.
- Individual skill lookup.
- Health-check and welcome endpoints.
- HTTP error handling for applicable missing resources.
- Interactive API documentation powered by FastAPI.

The features listed above reflect the intended current implementation and should be verified against the running application.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| FastAPI | REST API framework |
| Uvicorn | ASGI server |
| uv | Dependency and project management |
| Git and GitHub | Version control and source hosting |

Additional technologies will be introduced as the project develops.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | API health information |
| GET | `/profile` | Personal profile |
| GET | `/skills` | List available skills |
| GET | `/skills?category=programming` | Filter skills by category |
| GET | `/skills/category/{category_name}` | Retrieve skills in a category |
| GET | `/skills/{skill_name}` | Retrieve an individual skill |

## Getting Started

### Prerequisites

- Python 3.12 or a compatible version supported by the project
- Git
- uv

### 1. Clone the repository

```bash
git clone https://github.com/ReginaldErzoah/personal-api.git
cd personal-api
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Run the development server

```bash
uv run fastapi dev src/personal_api/main.py
```

The API will be available at `http://127.0.0.1:8000`.

### 4. Explore the API

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Project Structure

```text
personal-api/
├── src/
│   └── personal_api/
│       └── main.py
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

This represents the current application structure. Additional modules and directories will be introduced as the application grows.

## Current Limitations

- Skills are stored in memory.
- Professional information is not yet backed by persistent storage.
- The API primarily supports read operations.
- Automated testing, Docker containerisation, and deployment are planned enhancements unless otherwise implemented.

## Development Roadmap

The project will evolve toward a complete professional profile API with automated testing, containerisation, and deployment.

See [DEVELOPMENT_ROADMAP.md](DEVELOPMENT_ROADMAP.md) for the planned milestones, implementation tasks, and completion criteria.

## Author

**Reginald Erzoah**

- GitHub: http
