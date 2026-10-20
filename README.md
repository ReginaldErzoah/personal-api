# Personal API

A REST API built with **Python and FastAPI** to provide structured access to personal profile information and professional skills.

Personal API is a hands-on software engineering project focused on learning REST API design, HTTP request handling, routing, data filtering, error handling, and Python application structure. It forms part of my journey toward Data Engineering, MLOps, and building reliable data systems.

## Overview

Personal API exposes personal profile information and a collection of professional skills through HTTP endpoints. Clients can retrieve profile information, list skills, filter skills by category, and look up individual skills.

The project is being developed incrementally, with an emphasis on understanding API fundamentals before introducing more advanced engineering practices such as automated testing, persistent storage, containerisation, and continuous integration.

## Current Features

- Built with Python and FastAPI.
- Health-check endpoint.
- Personal profile endpoint.
- Skills listing endpoint.
- Category-based filtering using query parameters.
- Dedicated route for retrieving skills by category.
- Individual skill lookup.
- HTTP 404 error handling for resources that cannot be found.
- Interactive API documentation powered by FastAPI.

> Features listed here should reflect the behaviour implemented and tested in the current version.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and data handling |
| FastAPI | API development, routing, and request handling |
| Uvicorn | ASGI server for running the application |
| uv | Python project and dependency management |
| Git | Version control |
| GitHub | Source code hosting and collaboration |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns a welcome message |
| GET | `/health` | Returns API health information |
| GET | `/profile` | Retrieves personal profile information |
| GET | `/skills` | Retrieves all available skills |
| GET | `/skills?category=programming` | Filters skills by category |
| GET | `/skills/category/{category_name}` | Retrieves skills belonging to a category |
| GET | `/skills/{skill_name}` | Retrieves an individual skill by name |

### Example Requests

Retrieve the welcome message:

```http
GET /
```

Check API health:

```http
GET /health
```

Retrieve the profile:

```http
GET /profile
```

Retrieve all skills:

```http
GET /skills
```

Filter skills by category:

```http
GET /skills?category=programming
```

Retrieve skills in a category:

```http
GET /skills/category/data
```

Retrieve an individual skill:

```http
GET /skills/Python
```

The available categories and skill names depend on the application's data and matching logic.

## Error Handling

The API uses HTTP status codes to communicate the outcome of requests.

- `200 OK` — The request was processed successfully.
- `404 Not Found` — The requested skill or category could not be found, where applicable.

FastAPI also generates interactive API documentation and supports request validation through Python type annotations and other validation declarations.

## Getting Started

### Prerequisites

Install the following tools:

- Python 3.12 or a compatible version supported by the project.
- Git.
- uv.
- A terminal such as Git Bash, PowerShell, or a Linux shell.

### 1. Clone the repository

```bash
git clone https://github.com/ReginaldErzoah/personal-api.git
cd personal-api
```

### 2. Install project dependencies

From the project root, run:

```bash
uv sync
```

This installs the project's declared dependencies and synchronises its virtual environment.

### 3. Run the API

Start the development server:

```bash
uv run fastapi dev src/personal_api/main.py
```

The API should be available at:

`http://127.0.0.1:8000`

The development server automatically reloads the application when supported code changes are detected.

### 4. Explore the API

Open the interactive Swagger UI documentation:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Swagger UI allows you to inspect endpoints, provide query and path parameters, send requests, and examine responses.

Alternative documentation is available through ReDoc:

[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Structure

The current application entry point is `src/personal_api/main.py`.

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

This structure represents

## Current Limitations

The current version focuses on foundational API development.

- Skills are stored in an in-memory Python collection.
- Data is not persisted in a database.
- The API primarily supports retrieval operations rather than full CRUD functionality.
- Authentication and authorisation are not implemented.
- Automated testing, containerisation, and deployment are planned areas of development rather than established capabilities.

Because the skills data is held in memory, changes to that collection are not persisted across application restarts.

## Development Roadmap

Planned enhancements include:

- [ ] Introduce structured request and response models using Pydantic.
- [ ] Improve input validation and error handling.
- [ ] Add automated tests using pytest and an API test client.
- [ ] Implement create, update, and delete operations.
- [ ] Introduce persistent storage using SQLite or PostgreSQL.
- [ ] Separate routing, business logic, and data access into appropriate modules.
- [ ] Add configuration management and environment variables where needed.
- [ ] Containerise the application using Docker.
- [ ] Introduce Docker Compose if additional services are required.
- [ ] Automate quality checks and testing with GitHub Actions.
- [ ] Deploy the API and document its operational requirements.

These items represent planned improvements and are not claims about completed functionality.

## Learning Objectives

This project is intended to develop practical understanding of:

- Python programming and application structure.
- REST principles, HTTP methods, and status codes.
- FastAPI routing and parameter handling.
- Query-based filtering and resource retrieval.
- Input validation and exception handling.
- API documentation and manual testing.
- Automated testing and maintainable code.
- Database integration, containerisation, and deployment.

## Project Philosophy

The goal is not simply to build endpoints that return responses. It is to understand why an API is designed in a particular way, how requests move through an application, how errors should be handled, and how software can become reliable, testable, and maintainable.

Each enhancement should introduce a clear engineering concept and be validated before additional complexity is added.

## Author

**Reginald Erzoah**

GitHub: [ReginaldErzoah](https://github.com/ReginaldErzoah)
