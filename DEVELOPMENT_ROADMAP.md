# Personal API — Development Roadmap

## Project Goal

Build a reliable, well-tested, and containerized REST API that exposes my professional CV information, including my profile, skills, projects, experience, education, and certifications.

## Phase 1: Build the API

- [x] Set up the FastAPI project.
- [x] Create Pydantic models for API data.
- [x] Add sample data for my profile, skills, projects, and certifications.
- [x] Create endpoints to retrieve the available data.
- [x] Add lookup endpoints by name and ID where applicable.
- [x] Handle records that cannot be found using HTTP 404 errors.
- [x] Add experience and education data and endpoints.
- [ ] Review and improve code readability and organization.

## Phase 2: Learn API Testing

- [x] Install `pytest` and `httpx`.
- [x] Create a `tests/` directory.
- [x] Write tests for successful API requests.
- [x] Test response data and status codes.
- [x] Test missing records and invalid inputs.
- [x] Run all tests and fix any failures.

## Phase 3: Improve Code Quality

- [x] Follow Python's PEP 8 style guidelines.
- [x] Use Ruff for linting and formatting.
- [x] Use type hints consistently.
- [x] Improve error handling and input validation.
- [x] Organize code into separate modules when necessary.
- [x] Ensure all tests pass.

## Phase 4: Add Persistent Storage

- [ ] Understand the difference between in-memory data and a database.
- [ ] Choose a database, starting with SQLite or PostgreSQL.
- [ ] Design tables for the CV information.
- [ ] Connect the API to the database.
- [ ] Implement database read operations.
- [ ] Test database interactions.

## Phase 5: Containerize with Docker

- [ ] Understand Docker images and containers.
- [ ] Write a `Dockerfile`.
- [ ] Add a `.dockerignore` file.
- [ ] Build the Docker image.
- [ ] Run the API inside a container.
- [ ] Test the containerized API.
- [ ] Document how to build and run the container.

## Phase 6: Set Up CI with GitHub Actions

- [ ] Store the project in GitHub.
- [ ] Create a GitHub Actions workflow.
- [ ] Automatically run Ruff checks on pushes and pull requests.
- [ ] Automatically run tests.
- [ ] Fix any failing checks.
- [ ] Require successful checks before merging changes where practical.

## Phase 7: Deploy the API

- [ ] Choose a cloud hosting platform.
- [ ] Deploy the API.
- [ ] Configure environment variables where needed.
- [ ] Test the deployed endpoints using Postman.
- [ ] Verify the health endpoint.
- [ ] Document the live API URL and available endpoints.
- [ ] Update the README with deployment instructions.

## Phase 8: Build a Gradio Interface

- [ ] Understand what Gradio is and how it works with APIs.
- [ ] Install Gradio.
- [ ] Create a simple web interface for my professional profile.
- [ ] Display my skills, projects, experience, education, and certifications.
- [ ] Connect the Gradio interface to the Personal API using HTTP requests.
- [ ] Handle API errors and unavailable responses gracefully.
- [ ] Improve the interface layout and usability.
- [ ] Test the interface locally.
- [ ] Deploy the Gradio application.
- [ ] Document how the interface communicates with the API.

## Phase 9: Final Documentation and Portfolio

- [ ] Write a clear `README.md`.
- [ ] Document each API endpoint and its expected response.
- [ ] Add instructions for local development and testing.
- [ ] Document Docker, CI, and deployment workflows.
- [ ] Include example API requests and responses.
- [ ] Document the Gradio interface and provide its URL.
- [ ] Keep the repository organized and professional.
- [ ] Add the project to my portfolio and CV.


## Recommended Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [pytest Documentation](https://docs.pytest.org/en/stable/)
- [Pydantic Documentation](https://docs.pydantic.dev/latest/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Docker Get Started](https://docs.docker.com/get-started/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Postman Learning Center](https://learning.postman.com/)

## Development Principle

**Build -> Test -> Improve -> Containerize -> Automate -> Deploy -> Document**