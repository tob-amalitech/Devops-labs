# SPRINT 0 - PLANNING & SETUP

**Goal:** Establish project foundation, define architecture, and plan initial sprints.

## Product Vision
To provide a lightweight, reliable, and developer-friendly API for task management that serves as a gold standard for demonstrating Agile and DevOps best practices.

## Technical Stack & Architecture
**Stack:**
- **Language:** Python 3.9+
- **Framework:** Flask
- **Database:** SQLite (dev/test), extensible to PostgreSQL
- **Testing:** pytest, pytest-cov
- **Linting:** flake8
- **Containerization:** Docker
- **CI/CD:** GitHub Actions

**Architecture:**
3-Layer Architecture to ensure separation of concerns:
1.  **API Layer (`routes.py`)**: Handles HTTP requests/responses and routing.
2.  **Logic Layer**: (Implicit in routes/models for MVP, but logically separate) Business rules and validation.
3.  **Data Layer (`models.py`)**: Database interactions and schema definitions.

## Definition of Done (DoD)
- [ ] Code compiles/runs without errors
- [ ] Unit tests written and passing (min 80% coverage)
- [ ] Code linted using `flake8`
- [ ] Documentation updated (API docs, README)
- [ ] Feature implemented according to Acceptance Criteria
- [ ] PR reviewed and merged

---

## User Stories

### SPRINT 1 - Core CRUD Operations

**US-01: Create a Task**
- **As a** user
- **I want to** create a new task with a title and description
- **So that** I can track my work
- **Acceptance Criteria:**
    - POST `/tasks` endpoint accepts JSON payload
    - Title is required; description is optional
    - Default status is "To Do"
    - Returns 201 Created and the created task object
    - Invalid input returns 400 Bad Request
- **Estimate:** 3 pts

**US-02: Retrieve Tasks**
- **As a** user
- **I want to** view all tasks or a specific task
- **So that** I can see what I need to do
- **Acceptance Criteria:**
    - GET `/tasks` returns a list of all tasks
    - GET `/tasks/<id>` returns a single task
    - Returns 404 if task ID not found
    - Response includes id, title, description, status, created_at
- **Estimate:** 5 pts

**US-03: Update a Task**
- **As a** user
- **I want to** update the status or details of a task
- **So that** I can keep my list current
- **Acceptance Criteria:**
    - PUT/PATCH `/tasks/<id>` accepts JSON
    - Can update title, description, or status
    - Validation ensures status is valid (e.g., "To Do", "In Progress", "Done")
    - Returns 200 OK and updated object
    - Returns 404 if not found
- **Estimate:** 3 pts

### SPRINT 2 - Advanced Features & Quality

**US-04: Delete a Task**
- **As a** user
- **I want to** remove a task
- **So that** I can declutter my list
- **Acceptance Criteria:**
    - DELETE `/tasks/<id>` endpoint
    - Removes task from database
    - Returns 204 No Content on success
    - Returns 404 if task doesn't exist
- **Estimate:** 2 pts

**US-05: Automated Testing Framework**
- **As a** developer
- **I want to** have a comprehensive test suite
- **So that** I can ensure code quality and prevent regressions
- **Acceptance Criteria:**
    - Pytest configured
    - Unit tests for all models
    - Integration tests for all API endpoints
    - CI pipeline fails if tests fail
    - Coverage report generated
- **Estimate:** 5 pts

**US-06: Monitoring and Logging**
- **As a** developer
- **I want to** see application logs and health status
- **So that** I can debug issues and monitor availability
- **Acceptance Criteria:**
    - Health check endpoint `/health` returns 200 OK
    - Structured logging configured (INFO, ERROR levels)
    - Request/Response logging middleware
- **Estimate:** 3 pts

---

## Sprint Planning Summary
- **Sprint 1 Velocity Target:** 11 pts
- **Sprint 2 Velocity Target:** 10 pts
