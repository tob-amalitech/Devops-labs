# Project Retrospective

## Overall Assessment
The project successfully delivered a working Task Management API while strictly adhering to Agile and DevOps methodologies. The iterative Sprint approach allowed for adjustment to requirements and technical challenges (e.g., dependency compatibility).

## Key Wins
1.  **TDD Discipline**: Writing tests first (e.g., for `DELETE` and `UPDATE` endpoints) clarified requirements and ensured the implementation met the exact acceptance criteria.
2.  **DevOps Integration**: Integrating CI (GitHub Actions) and Docker from the start reduced "works on my machine" issues.
3.  **Robustness**: Adding comprehensive error handling and logging in Sprint 2 significantly improved the production-readiness of the application.

## Challenges & Lessons Learned
-   **Dependency Management**: We encountered compatibility issues with `Flask 2.3.2` and `pytest 7.x` on modern Python environments.
    -   *Lesson*: Always pin dependencies but be prepared to upgrade for modern compatibility (moved to Flask 3.x and pytest 9.x).
-   **Shell Differences**: Running commands across different shells (PowerShell vs Bash) requires care (e.g., chaining commands with `;` vs `&&`).

## Metrics Summary
-   **Total Sprints**: 2
-   **User Stories Completed**: 6/6
-   **Test Pass Rate**: 100%
-   **Documentation Coverage**: Complete (Readme, Sprint docs, API specs)

## Future Roadmap
-   Add Authentication (JWT).
-   Migrate to PostgreSQL for production.
-   Add Swagger/OpenAPI documentation.
