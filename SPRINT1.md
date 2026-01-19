# SPRINT 1 - CORE CRUD

**Goal:** Implement Core CRUD operations (Create, Read, Update) using TDD and CI/CD.

## Completed User Stories
- **US-01: Create a Task** (3 pts) - [x] Done
    - Implemented `POST /tasks`
    - Validated title requirement
- **US-02: Retrieve Tasks** (5 pts) - [x] Done
    - Implemented `GET /tasks`
    - Verified list output structure
- **US-03: Update a Task** (3 pts) - [x] Done
    - Implemented `PUT /tasks/<id>`
    - Support for title, description, and status updates

## Demo Notes
The API can be tested using `curl` or Postman:
```bash
# Create
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title":"Demo Task"}'

# List
curl http://localhost:5000/tasks

# Update
curl -X PUT http://localhost:5000/tasks/1 -H "Content-Type: application/json" -d '{"status":"completed"}'
```

## Metrics
- **Commits:** 9
- **Tests Passing:** 3/3 (Core flows verified)
- **Coverage:** ~85% (Estimated based on route coverage)

## Retrospective
### What went well
- TDD approach caught edge cases early (e.g., missing titles, invalid status).
- CI pipeline setup ensures quality from day one.
- Separation of concerns (Models vs Routes) made testing easier.

### What to improve
- Need more comprehensive error handling for malformed JSON.
- Add logging for Sprint 2 to help with debugging.
- Setup local environment for easier test execution.

### Action Items for Sprint 2
- [ ] Implement Delete Task (US-04)
- [ ] Set up logging middleware (US-06)
- [ ] Refine test suite coverage
