# Personal API - Development Roadmap

## Goal

Build a professional CV API that exposes structured career information through a documented REST interface and can be reliably tested, containerised, and deployed.

The roadmap prioritises understanding, maintainability, and reproducibility over adding technologies without a clear purpose.

## Phase 1 - Stabilise the Existing API

- [ ] Review the current implementation in `src/personal_api/main.py`.
- [ ] Understand HTTP methods, status codes, JSON responses, query parameters, and path parameters.
- [ ] Verify every existing endpoint manually.
- [ ] Confirm that skill and category filtering returns the expected results.
- [ ] Resolve route-matching conflicts and parameter naming inconsistencies.
- [ ] Define behaviour for missing resources, empty values, and case sensitivity.
- [ ] Verify that errors return appropriate HTTP status codes.
- [ ] Commit a working baseline to Git.

**Done when:** Existing endpoints behave predictably and their request and response behaviour is understood.

## Phase 2 - Design the CV Data Model and API Contract

- [ ] Define the resources the API will expose:
  - Profile
  - Skills
  - Professional experience
  - Projects
  - Education
  - Certifications and training
  - Achievements
- [ ] Decide which information is public and appropriate to expose.
- [ ] Design representative JSON responses for each resource.
- [ ] Define consistent field names, data types, dates, and identifiers.
- [ ] Decide how related resources will reference one another.
- [ ] Define collection endpoints and individual-resource endpoints.
- [ ] Specify filtering, sorting, and pagination requirements where useful.
- [ ] Define consistent error-response behaviour.
- [ ] Decide whether the public API will be read-only.
- [ ] Review the proposed endpoint paths and response structures before implementation.

**Done when:** The API contract describes the intended resources, fields, routes, and error behaviour.

## Phase 3 - Implement Structured Schemas

- [ ] Learn and apply Pydantic models.
- [ ] Create schemas for profile, skills, projects, experience, education, certifications, and achievements.
- [ ] Define required fields, optional fields, defaults, and validation constraints.
- [ ] Use suitable types for dates, URLs, identifiers, and collections.
- [ ] Apply FastAPI response models to implemented endpoints.
- [ ] Introduce request models if write operations are required.
- [ ] Separate internal data structures from public response schemas where necessary.
- [ ] Verify invalid values and malformed data are handled appropriately.
- [ ] Confirm that private or internal fields cannot leak into public responses.

**Done when:** Implemented resources have explicit schemas and predictable response structures.

## Phase 4 — Build the Complete CV API

- [ ] Expand the profile with a professional headline, summary, and public links.
- [ ] Represent skills with categories, descriptions, and evidence of application.
- [ ] Add professional experience with roles, dates, responsibilities, and substantiated outcomes.
- [ ] Add projects with descriptions, technologies, repository links, and results.
- [ ] Add education, certifications, training, and achievements.
- [ ] Implement list and individual-resource endpoints.
- [ ] Implement useful resource filtering.
- [ ] Design a consolidated `/resume` endpoint if it benefits clients.
- [ ] Keep the professional data accurate and straightforward to update.
- [ ] Verify the behaviour and documentation of each new endpoint.

**Done when:** Clients can retrieve a coherent, machine-readable representation of the CV.

## Phase 5 — Refactor the Application

- [ ] Move route definitions into dedicated router modules.
- [ ] Organise Pydantic schemas into appropriate modules.
- [ ] Separate business logic from HTTP request handling.
- [ ] Introduce a data-access layer where appropriate.
- [ ] Keep the application entry point focused on creating the application and registering routers.
- [ ] Apply consistent naming, type annotations, and imports.
- [ ] Use dependency injection where it provides a clear benefit.
- [ ] Avoid duplicated logic and unnecessary abstractions.
- [ ] Verify existing functionality after refactoring.

**Done when:** Modules have clear responsibilities and the application can grow without concentrating all logic in `main.py`.

## Phase 6 — Choose and Implement Data Storage

- [ ] Evaluate whether version-controlled structured data files are sufficient for a public, read-only CV API.
- [ ] If persistence is justified, choose SQLite or PostgreSQL based on the requirements.
- [ ] Learn relational modelling, primary keys, foreign keys, and constraints.
- [ ] Design tables and relationships for the selected resources.
- [ ] Implement the database connection and data-access layer.
- [ ] Separate database models from API schemas where appropriate.
- [ ] Introduce migrations if required.
- [ ] Configure database connections through environment variables.
- [ ] Handle database errors and missing records.
- [ ] Test database operations against an isolated test database.
- [ ] Document database setup and recovery procedures where applicable.

**Done when:** The selected data source is reliable, maintainable, and testable. A database is optional if structured files adequately meet the product's requirements.

## Phase 7 — Automated Testing and Code Quality

- [ ] Add pytest and HTTPX as development dependencies.
- [ ] Create a `tests/` directory.
- [ ] Test every implemented endpoint's successful responses.
- [ ] Test missing resources, invalid parameters, and boundary cases.
- [ ] Verify response schemas and HTTP status codes.
- [ ] Test resource filtering and relationships.
- [ ] Use pytest fixtures for reusable test setup.
- [ ] Isolate tests from production data.
- [ ] Configure Ruff for linting and formatting.
- [ ] Run tests and quality checks from a clean environment.
- [ ] Generate coverage reports and review untested behaviour.
- [ ] Ensure tests are deterministic and do not depend on local machine state.

**Done when:** Automated tests and code-quality checks run consistently and detect regressions.

## Phase 8 — Production Configuration and Application Behaviour

- [ ] Separate development, testing, and production configuration.
- [ ] Define environment variables and sensible defaults.
- [ ] Keep secrets and credentials outside source control.
- [ ] Validate required settings at startup.
- [ ] Configure useful application logging.
- [ ] Avoid exposing stack traces and sensitive information to API clients.
- [ ] Review startup and shutdown behaviour.
- [ ] Define liveness and readiness checks where appropriate.
- [ ] Confirm the production server command works.
- [ ] Document supported Python versions and dependency installation.

**Done when:** The application can run with explicit configuration and predictable operational behaviour.

## Phase 9 — Docker Containerisation

- [ ] Understand images, containers, layers, ports, networks, and volumes.
- [ ] Create a `Dockerfile`.
- [ ] Choose an appropriate Python base image.
- [ ] Create `.dockerignore` to exclude `.venv`, `.git`, caches, secrets, and unnecessary files.
- [ ] Structure the Dockerfile to make dependency installation cacheable.
- [ ] Install dependencies reproducibly using the project configuration and lockfile.
- [ ] Ensure the `src`-layout package is installed or otherwise importable inside the image.
- [ ] Configure the application to listen on `0.0.0.0` inside the container.
- [ ] Use an appropriate production server command.
- [ ] Run the application as a non-root user where practical.
- [ ] Supply configuration at runtime rather than embedding secrets in the image.
- [ ] Configure a useful container health check where supported.
- [ ] Build the image from the repository root.
- [ ] Run the container with an appropriate port mapping.
- [ ] Verify API routes and health behaviour from the host.
- [ ] Inspect container logs, exit behaviour, and restart behaviour.
- [ ] Rebuild the image from a clean checkout.
- [ ] Review image size and known vulnerabilities.
- [ ] Document build, run, stop, inspection, and cleanup commands.

**Done when:** The image builds reproducibly and the API runs independently of the host's Python environment.

## Phase 10 — Docker Compose (When Required)

- [ ] Decide whether the application needs coordinated services.
- [ ] Create `compose.yaml` if a database or other supporting service is required.
- [ ] Define services, ports, networks, environment variables, and volumes.
- [ ] Configure service readiness rather than relying solely on startup order.
- [ ] Add health checks where useful.
- [ ] Persist database data when applicable.
- [ ] Keep local environment files and secrets out of source control.
- [ ] Test service-to-service communication.
- [ ] Verify behaviour after containers are recreated.
- [ ] Document startup, shutdown, and rebuild commands.

**Done when:** Required services can be started and operated consistently through a documented Compose workflow.

## Phase 11 — Continuous Integration with GitHub Actions

- [ ] Create a workflow under `.github/workflows/`.
- [ ] Trigger the workflow on relevant pushes and pull requests.
- [ ] Set up the supported Python version.
- [ ] Install project dependencies reproducibly.
- [ ] Run Ruff linting and formatting checks.
- [ ] Run pytest.
- [ ] Fail the workflow when required checks fail.
- [ ] Build the Docker image in CI.
- [ ] Ensure tests do not depend on private local files.
- [ ] Add dependency or container vulnerability checks where practical.
- [ ] Apply least-privilege workflow permissions.
- [ ] Verify both successful and failing workflow runs.

**Done when:** Code changes are automatically checked and invalid changes cannot pass the required quality gates.

## Phase 12 — Deployment

- [ ] Select a container-compatible hosting platform that fits the budget.
- [ ] Understand its port, configuration, health-check, and startup requirements.
- [ ] Select a container registry if required.
- [ ] Configure image publishing and deployment credentials securely.
- [ ] Deploy a verified image.
- [ ] Configure HTTPS.
- [ ] Verify the deployed endpoints and response schemas.
- [ ] Test the public health endpoint and interactive documentation.
- [ ] Confirm the service starts correctly after redeployment.
- [ ] Review usage limits, costs, and shutdown procedures.
- [ ] Document deployment and recovery steps.
- [ ] Test the deployed service after each release.

**Done when:** The API is accessible over HTTPS, operates as expected, and can be redeployed through documented procedures.

## Phase 13 — Release and Delivery Workflow

- [ ] Establish a simple branching and pull-request strategy.
- [ ] Define release tags and versioning conventions.
- [ ] Tag container images so releases can be identified.
- [ ] Publish images only after required CI checks pass.
- [ ] Automate deployment where supported.
- [ ] Run smoke tests against the deployed service.
- [ ] Separate staging and production environments if justified.
- [ ] Store deployment credentials in appropriate secret-management facilities.
- [ ] Document rollback and recovery procedures.
- [ ] Verify that failed checks prevent an unverified release.

**Done when:** Releases follow a repeatable workflow with automated verification and a documented recovery strategy.

## Phase 14 — Final Documentation and Portfolio Readiness

- [ ] Keep `README.md` focused on the product, current features, setup, and usage.
- [ ] Maintain this file as the detailed implementation roadmap.
- [ ] Document architecture and module responsibilities.
- [ ] Document endpoint contracts, examples, and error responses.
- [ ] Include testing and Docker instructions.
- [ ] Document configuration variables without exposing secrets.
- [ ] Add an architecture diagram if useful.
- [ ] Add CI status and live API links when available.
- [ ] Verify repository and deployment links.
- [ ] Remove unused code and unnecessary dependencies.
- [ ] Add a licence if appropriate.
- [ ] Test setup instructions from a clean checkout.
- [ ] Ensure the documented capabilities match the actual implementation.

**Done when:** Another developer can understand the project, run it, test it, build the container, and access the deployed API using the documentation.

## Final Acceptance Criteria

The project is ready to be presented as a completed containerised API portfolio project when:

- [ ] The public CV resources are implemented and documented.
- [ ] Response schemas and error behaviour are consistent.
- [ ] Automated tests and code-quality checks pass.
- [ ] Configuration and public data exposure have been reviewed.
- [ ] The Docker image builds reproducibly.
- [ ] The container runs independently of the host development environment.
- [ ] Docker Compose is provided if the application requires multiple services.
- [ ] GitHub Actions automates the required quality checks and image build.
- [ ] The deployed service is accessible and verified.
- [ ] Setup, testing, containerisation, deployment, and recovery instructions are documented.

## Guiding Principle

Every milestone should solve a clear problem and build on skills established in earlier milestones. Add complexity only when it serves the product or demonstrates a meaningful engineering capability.

The goal is to develop both a useful professional CV API and the ability to independently engineer, test, containerise, and deliver reliable software.
