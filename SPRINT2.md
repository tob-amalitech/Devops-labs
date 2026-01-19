# SPRINT 2 - DEVOPS & READINESS

**Goal:** Add DevOps tooling, monitoring, and production readiness.

## Completed User Stories
- **US-04: Delete a Task** (2 pts) - [x] Done
    - Implemented `DELETE /tasks/<id>`
    - Added comprehensive test coverage
- **US-05: Automated Testing Framework** (5 pts) - [x] Done
    - Added integration tests (`test_full_workflow`)
    - Added edge case testing (Invalid IDs, Payloads)
    - Achieved >85% coverage
- **US-06: Monitoring and Logging** (3 pts) - [x] Done
    - Implemented Request/Response logging middleware
    - Added INFO level logging to routes

## DevOps Practices Demonstrated
- [x] **CI/CD Pipeline:** GitHub Actions configured for Test/Lint/Build
- [x] **Containerization:** Dockerfile and simple docker-compose setup
- [x] **TDD:** Strict Red-Green-Refactor cycle followed
- [x] **Infrastructure as Code:** Configuration via files (requirements.txt, Dockerfile)

## Metrics
- **Total Commits:** 15+
- **Tests Passing:** 7/7 (100%)
- **Code Coverage:** High (All routes covered)

## Retrospective
### What went well
- TDD workflow prevented regressions when refactoring.
- Docker setup was straightforward.
- Logging middleware immediately provided visibility.

### What to improve
- `pytest` configuration needed adjustment for newer Python versions.
- Initial error handling was too basic; `try/except` blocks added robustness.

### Action Items
- [ ] Set up a staging environment.
- [ ] Add more granular unit tests for models.
