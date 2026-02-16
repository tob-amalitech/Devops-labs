# Task Management REST API

## 📋 Project Overview

### Product Vision Statement
**Deliver a lightweight, developer-friendly REST API for task management that exemplifies Agile development practices and modern DevOps methodologies, serving as an educational reference for building production-ready applications.**

This project demonstrates how to combine test-driven development, continuous integration/continuous deployment, containerization, and iterative sprint-based development to create a maintainable, scalable application.

### Technology Stack
- **Language**: Python 3.9+
- **Web Framework**: Flask 3.0+
- **Database**: SQLite (Development/Testing) - extensible to PostgreSQL
- **Testing Framework**: pytest 8.0+, pytest-cov
- **Code Quality Tools**: flake8, Black
- **Containerization**: Docker, Docker Compose
- **CI/CD Platform**: GitHub Actions
- **Logging**: Python logging module
- **API Design Pattern**: RESTful architecture with JSON payloads

### Project Goals & Objectives
1. **Demonstrate Agile Best Practices**: Implement Scrum methodology with structured sprints (Sprint 0/1/2) and regular retrospectives
2. **Showcase DevOps Culture**: Automated testing, CI/CD pipelines, infrastructure-as-code (Docker), and monitoring
3. **Ensure Code Quality**: Maintain >85% test coverage, enforce linting standards, and implement comprehensive error handling
4. **Build Production-Ready Software**: Implement logging, health checks, Docker containerization, and graceful error handling
5. **Document Iterative Development**: Provide clear evidence of incremental development and continuous improvement

## Agile & DevOps Practices Implemented
This project serves as a reference implementation for:

✅ **Agile Methodology**: 3-Sprint development cycle with user stories, story points, and sprint planning
✅ **Test-Driven Development (TDD)**: Tests written first, following the Red-Green-Refactor cycle
✅ **CI/CD Pipeline**: Automated GitHub Actions workflow for testing, linting, and code quality checks
✅ **Automated Testing**: Comprehensive test suite using pytest with >85% coverage
✅ **Containerization**: Fully Dockerized with multi-stage build optimization
✅ **Infrastructure as Code**: Docker Compose for local development environment
✅ **Logging & Monitoring**: Request/response logging, error tracking, health checks
✅ **Code Quality**: Enforced PEP 8 linting with flake8
✅ **Git Workflow**: Conventional commits (feat, test, fix, docs, build, refactor)
✅ **Documentation**: Comprehensive project, sprint, and technical documentation
✅ **Error Handling**: Structured exception handling with appropriate HTTP status codes
✅ **Database Management**: SQLAlchemy ORM for database operations and migrations

## 📊 Project Status
| Sprint | Status | Duration | Focus Area |
|--------|--------|----------|-----------|
| **Sprint 0** | ✅ Completed | Planning | Project setup, architecture, backlog creation |
| **Sprint 1** | ✅ Completed | Week 1-2 | Core CRUD operations, initial testing |
| **Sprint 2** | ✅ Completed | Week 3-4 | DevOps tooling, monitoring, production readiness |

📖 **Detailed Documentation**: See [SPRINT0.md](SPRINT0.md), [SPRINT1.md](SPRINT1.md), [SPRINT2.md](SPRINT2.md), and [TECHNICAL_DOCUMENTATION.md](TECHNICAL_DOCUMENTATION.md)

## 🔌 API Documentation

The API follows RESTful conventions with JSON request/response payloads.

### Endpoints Summary

| Method | Endpoint | Description | Status Codes |
|--------|----------|-------------|--------------|
| `POST` | `/tasks` | Create a new task | 201, 400 |
| `GET` | `/tasks` | List all tasks | 200 |
| `GET` | `/tasks/<id>` | Get task by ID | 200, 404 |
| `PUT` | `/tasks/<id>` | Update task | 200, 400, 404 |
| `DELETE` | `/tasks/<id>` | Delete task | 204, 404 |

### Detailed Endpoint Documentation

See [TECHNICAL_DOCUMENTATION.md](TECHNICAL_DOCUMENTATION.md#-api-endpoints) for complete API specifications including request/response examples and error handling.

## 🚀 Getting Started

### Prerequisites
- Python 3.9+ (included in Docker if using containerization)
- Docker & Docker Compose (optional, for containerized deployment)
- Git for version control

### Quick Start: Local Installation

**Step 1: Clone and navigate to project**
```bash
git clone <repository-url>
cd Devops-labs
```

**Step 2: Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 3: Run the application**
```bash
python app.py
```
The API will be accessible at `http://localhost:5000`

### Quick Start: Using Docker Compose

**One-command setup and run:**
```bash
docker-compose up --build
```
The API will be accessible at `http://localhost:5000`

## ✅ Testing & Verification

### Run Automated Test Suite
```bash
python -m pytest -v --cov=app --cov-report=term-missing
```
Expected output: **7/7 tests passing** with **>85% code coverage**

### Manual API Testing

#### Using PowerShell (Windows)
```powershell
# Create a task
Invoke-RestMethod -Method POST -Uri http://localhost:5000/tasks `
  -ContentType "application/json" `
  -Body '{"title":"My Task","description":"Task details"}'

# List all tasks
Invoke-RestMethod -Uri http://localhost:5000/tasks

# Update task (set status to completed)
Invoke-RestMethod -Method PUT -Uri http://localhost:5000/tasks/1 `
  -ContentType "application/json" `
  -Body '{"status":"completed"}'

# Delete task
Invoke-RestMethod -Method DELETE -Uri http://localhost:5000/tasks/1
```

#### Using curl/bash (Linux/macOS)
```bash
# Create a task
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"My Task","description":"Task details"}'

# List all tasks
curl http://localhost:5000/tasks

# Update task
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"completed"}'

# Delete task
curl -X DELETE http://localhost:5000/tasks/1
```

## 📁 Project Structure
```
Devops-labs/
├── app/                          # Application source code
│   ├── __init__.py              # Flask app factory
│   ├── models.py                # Database models (Task)
│   └── routes.py                # API endpoints and business logic
├── tests/                        # Test suite
│   ├── conftest.py              # Pytest fixtures
│   ├── test_routes.py           # Integration tests
│   └── __pycache__/
├── instance/                     # Runtime instance data (SQLite DB)
├── Dockerfile                    # Container image definition
├── docker-compose.yml           # Local development environment
├── requirements.txt             # Python dependencies
├── app.py                        # Application entry point
├── README.md                     # This file - project overview
├── SPRINT0.md                    # Planning & setup documentation
├── SPRINT1.md                    # Sprint 1 execution documentation
├── SPRINT2.md                    # Sprint 2 execution documentation
├── TECHNICAL_DOCUMENTATION.md   # Architecture, setup, and deployment
└── RETROSPECTIVE.md             # Final project retrospective
```

## 📖 Documentation Guide

**Start Here:**
- [README.md](README.md) (this file) - Project overview and quick start

**Planning & Requirements:**
- [SPRINT0.md](SPRINT0.md) - Product backlog, user stories, DoD, and technical architecture

**Development & Execution:**
- [SPRINT1.md](SPRINT1.md) - Core CRUD implementation, testing, and CI/CD
- [SPRINT2.md](SPRINT2.md) - Advanced features, monitoring, and production readiness

**Technical Deep Dive:**
- [TECHNICAL_DOCUMENTATION.md](TECHNICAL_DOCUMENTATION.md) - Architecture, API details, deployment, and troubleshooting

**Retrospectives & Lessons:**
- [RETROSPECTIVE.md](RETROSPECTIVE.md) - Overall project retrospective and future roadmap

## 🔗 Key Links & Resources

| Resource | Purpose |
|----------|---------|
| [SPRINT0.md](SPRINT0.md) | Product backlog and stakeholder alignment |
| [SPRINT1.md](SPRINT1.md) | Sprint 1 deliverables and testing evidence |
| [SPRINT2.md](SPRINT2.md) | Sprint 2 improvements and DevOps implementation |
| [TECHNICAL_DOCUMENTATION.md](TECHNICAL_DOCUMENTATION.md) | Architecture, deployment guides, troubleshooting |
| [RETROSPECTIVE.md](RETROSPECTIVE.md) | Lessons learned and future roadmap |

## 📊 Metrics & Achievement Summary

| Metric | Target | Achieved |
|--------|--------|----------|
| Test Coverage | >80% | 85%+ ✅ |
| User Stories Completed | 6/6 | 6/6 ✅ |
| Test Pass Rate | 100% | 100% ✅ |
| Sprints Completed | 3 | 3 ✅ |
| Documentation Complete | Yes | Yes ✅ |
| CI/CD Pipeline | Yes | Yes ✅ |
| Containerization | Yes | Yes ✅ |

## ⚡ Quick Command Reference

```bash
# Setup
pip install -r requirements.txt

# Run locally
python app.py

# Run tests with coverage
python -m pytest -v --cov=app --cov-report=html

# Lint code
flake8 app/ tests/

# Build & run Docker
docker-compose up --build

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## 🤝 Contributing & Development Workflow

This project follows Agile methodology with sprint-based development:

1. **Sprint Planning**: Define user stories and acceptance criteria
2. **Development**: Implement features using TDD (write tests first)
3. **Testing**: Execute comprehensive test suite
4. **Code Review**: Peer review via pull requests
5. **Deployment**: Automated via CI/CD pipeline
6. **Sprint Review**: Demonstrate completed work
7. **Retrospective**: Reflect on process and identify improvements

For detailed development guidelines, see the appropriate sprint documentation.

## 📝 License & Support

For questions or issues, please refer to the detailed documentation files or create an issue in the repository.

---

**Last Updated**: February 2026 | **Version**: 2.0 | **Status**: Production Ready