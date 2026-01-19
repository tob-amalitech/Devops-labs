# Task Management REST API

## Overview
A robust, production-ready REST API for task management, built to demonstrate modern **Agile** and **DevOps** best practices. This project uses Python, Flask, and SQLite, wrapped in a Docker container, and follows a strict TDD lifecycle.

## Agile & DevOps Practices
This project serves as a reference implementation for:

✅ **CI/CD Pipeline**: GitHub Actions workflow (`.github/workflows/ci.yml`) for automated testing and linting.
✅ **Automated Testing**: Comprehensive test suite using `pytest` (>85% coverage).
✅ **Test-Driven Development (TDD)**: Verified commit history showing "test:" before "feat:".
✅ **Containerization**: Fully Dockerized application (`Dockerfile`, `docker-compose.yml`).
✅ **Logging & Monitoring**: Integrated Request/Response logging and error tracking.
✅ **Code Quality**: Enforced via `flake8` and adherence to PEP 8.
✅ **Version Control**: Conventional commits (feat, test, fix, build, docs).

## Project Status
- **Sprint 0**: Planning & Setup (Completed)
- **Sprint 1**: Core CRUD (Completed)
- **Sprint 2**: DevOps & Polish (Completed)

See [SPRINT0.md](SPRINT0.md), [SPRINT1.md](SPRINT1.md), and [SPRINT2.md](SPRINT2.md) for detailed planning and retrospectives.

## API Documentation

| Method | Endpoint | Description | Payload |
| :--- | :--- | :--- | :--- |
| `POST` | `/tasks` | Create a new task | `{"title": "Task", "description": "..."}` |
| `GET` | `/tasks` | List all tasks | N/A |
| `GET` | `/tasks/<id>` | Get task details | N/A |
| `PUT` | `/tasks/<id>` | Update task | `{"status": "completed"}` |
| `DELETE` | `/tasks/<id>` | Delete task | N/A |
| `GET` | `/health` | Health Check | N/A |

## Getting Started

### Prerequisites
- Python 3.9+
- Docker (optional)

### Local Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd task-manager-api
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

### Running Tests
Execute the test suite including integration tests:
```bash
python -m pytest
```

### Running with Docker
Build and run using Docker Compose:
```bash
docker-compose up --build
```
Access the API at `http://localhost:5000`.
