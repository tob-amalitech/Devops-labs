# TECHNICAL DOCUMENTATION

**Version**: 2.0  
**Last Updated**: February 2026  
**Status**: Production Ready  

---

## Table of Contents

1. [Architecture Overview](#-architecture-overview)
2. [Development Environment Setup](#-development-environment-setup)
3. [API Endpoints](#-api-endpoints)
4. [Database Schema](#-database-schema)
5. [Deployment Process](#-deployment-process)
6. [Monitoring & Troubleshooting](#-monitoring--troubleshooting)
7. [Security Considerations](#-security-considerations)
8. [Performance Optimization](#-performance-optimization)

---

## 🏗️ Architecture Overview

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                       Client Applications                        │
│  (Web Browsers, Mobile Apps, Third-party Services, etc.)        │
└────────────────────┬────────────────────────────────────────────┘
                     │ HTTP/REST
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Load Balancer (Optional)                    │
│              (For high-availability deployments)                │
└────────────────────┬────────────────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   ┌─────────┬─────────┬─────────┐
   │ API    │ API    │ API    │  (Multiple instances for scale)
   │Server 1│Server 2│Server N│
   └────┬────┴────┬────┴────┬────┘
        │         │         │
        └─────────┼─────────┘
                  ▼
        ┌─────────────────────┐
        │  Request Logging    │
        │  & Validation       │
        └──────────┬──────────┘
                   │
        ┌──────────▼─────────────┐
        │  Flask Application     │
        │  ┌────────────────────┐│
        │  │  Routes Layer      ││ (HTTP handlers)
        │  │  ┌──────────────┐  ││
        │  │  │ POST /tasks  │  ││
        │  │  │ GET /tasks   │  ││
        │  │  │ PUT /tasks   │  ││
        │  │  │ DELETE/tasks │  ││
        │  │  └──────────────┘  ││
        │  └────────────────────┘│
        │  ┌────────────────────┐│
        │  │  Models Layer      ││ (ORM & Validation)
        │  │  ┌──────────────┐  ││
        │  │  │ Task Model   │  ││
        │  │  │ Validation   │  ││
        │  │  └──────────────┘  ││
        │  └────────────────────┘│
        └──────────┬──────────────┘
                   │
        ┌──────────▼─────────────┐
        │  SQLAlchemy ORM        │
        │  (Database Abstraction) │
        └──────────┬──────────────┘
                   │
        ┌──────────▼─────────────┐
        │   SQLite/PostgreSQL    │
        │   (Persistent Storage) │
        └────────────────────────┘

Logging Flow:
  All Layers → Python logging module → stdout/file handlers → Log Aggregation
```

### 3-Layer Architecture Pattern

**Layer 1: API Layer** (`routes.py`)
- Responsible for: HTTP protocol handling, request routing, input validation
- Receives HTTP requests and returns JSON responses
- Handles authentication/authorization (TODO)
- Logging of all requests and responses
- Error handling with appropriate HTTP status codes

**Layer 2: Business Logic Layer** (Implicit in routes/models)
- Responsible for: Business rules enforcement, data validation, transformation
- Ensures task status update only to valid values
- Enforces title as required field
- Coordinates between API and data layers

**Layer 3: Data Layer** (`models.py`)
- Responsible for: Database schema, CRUD operations, data persistence
- SQLAlchemy ORM models define schema
- Database transactions and constraints
- Data serialization (`.to_dict()` method)

---

## 🛠️ Development Environment Setup

### Prerequisites

**Required Software**:
- Python 3.9+ (download from python.org)
- Git (download from git-scm.com)
- pip (included with Python)

**Optional but Recommended**:
- Docker & Docker Compose (for containerized development)
- Visual Studio Code with Python extension
- Postman or Insomnia (for API testing)

### Local Development Setup

**Step 1: Clone Repository**
```bash
git clone <repository-url>
cd Devops-labs
```

**Step 2: Create Virtual Environment** (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**Step 3: Install Dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Step 4: Initialize Database**
```bash
# Database is auto-created on first run, but you can manually initialize:
python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all()"
```

**Step 5: Run Application**
```bash
python app.py
# Or using Flask CLI:
flask run
```

The app will be available at `http://localhost:5000`

**Step 6: Run Tests**
```bash
# Run all tests with coverage
pytest -v --cov=app --cov-report=term-missing --cov-report=html

# Run specific test file
pytest tests/test_routes.py -v

# Run with verbose output
pytest -vv
```

### Environment Variables

**Local Development** (`.env`):
```bash
FLASK_APP=app
FLASK_ENV=development
DATABASE_URL=sqlite:///instance/tasks.db
LOG_LEVEL=INFO
```

**Production** (Kubernetes/Docker):
```bash
FLASK_APP=app
FLASK_ENV=production
DATABASE_URL=postgresql://user:pass@db-host/dbname
LOG_LEVEL=WARNING
WORKERS=4
```

### Project Structure Explained

```
Devops-labs/
├── app/
│   ├── __init__.py          # Flask app factory & initialization
│   ├── models.py            # SQLAlchemy models (ORM)
│   ├── routes.py            # API endpoints & business logic
│   └── __pycache__/
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # pytest fixtures (setup/teardown)
│   ├── test_routes.py       # Integration & unit tests
│   └── __pycache__/
├── instance/                # Runtime data directory (SQLite DB)
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI/CD config
├── Dockerfile               # Container image definition
├── docker-compose.yml       # Local dev environment
├── app.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── README.md                # Project overview
├── SPRINT0.md               # Planning documentation
├── SPRINT1.md               # Sprint 1 execution docs
├── SPRINT2.md               # Sprint 2 execution docs
├── RETROSPECTIVE.md         # Final project retrospective
└── TECHNICAL_DOCUMENTATION.md (this file)
```

---

## 🔌 API Endpoints

### Base URL
```
Local Development: http://localhost:5000
Docker Container:  http://localhost:5000
Production:        https://api.example.com (adjust for your deployment)
```

### Authentication
Currently, no authentication is implemented. **TODO**: Implement JWT token-based auth.

### Response Format
All responses are JSON. Successful operations return with HTTP 2xx status codes. Errors return 4xx or 5xx status codes with error messages.

---

### 1. Create Task

**Endpoint**: `POST /tasks`  
**Description**: Create a new task  
**Authentication**: None (add JWT in future)

**Request Headers**:
```
Content-Type: application/json
```

**Request Body**:
```json
{
  "title": "Complete project documentation",
  "description": "Add comprehensive technical documentation for the task API"
}
```

**Request Parameters**:
```
title (string, required): Task title (max 100 characters)
description (string, optional): Task description (max 200 characters)
```

**Response** (Status: 201 Created):
```json
{
  "id": 1,
  "title": "Complete project documentation",
  "description": "Add comprehensive technical documentation for the task API",
  "status": "pending",
  "created_at": "2026-02-16T10:23:45.123456"
}
```

**Error Responses**:
```json
// 400 Bad Request - Missing title
{
  "error": "Title is required"
}

// 400 Bad Request - Malformed JSON
{
  "error": "Invalid JSON"
}

// 500 Internal Server Error - Database error
{
  "error": "Database error"
}
```

**Example Requests**:

PowerShell:
```powershell
$body = @{
    title = "Learn Docker"
    description = "Study Docker containerization concepts"
} | ConvertTo-Json

Invoke-RestMethod -Method POST `
  -Uri http://localhost:5000/tasks `
  -ContentType "application/json" `
  -Body $body
```

curl/bash:
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn Docker",
    "description": "Study Docker containerization concepts"
  }'
```

---

### 2. List All Tasks

**Endpoint**: `GET /tasks`  
**Description**: Retrieve all tasks  
**Authentication**: None

**Query Parameters**: None

**Response** (Status: 200 OK):
```json
[
  {
    "id": 1,
    "title": "Learn Docker",
    "description": "Study Docker containerization concepts",
    "status": "pending",
    "created_at": "2026-02-16T10:23:45.123456"
  },
  {
    "id": 2,
    "title": "Complete Documentation",
    "description": "Write comprehensive technical docs",
    "status": "completed",
    "created_at": "2026-02-16T10:25:00.000000"
  }
]
```

**Example Requests**:

PowerShell:
```powershell
Invoke-RestMethod -Uri http://localhost:5000/tasks
```

curl/bash:
```bash
curl http://localhost:5000/tasks
```

---

### 3. Get Single Task

**Endpoint**: `GET /tasks/<id>`  
**Description**: Retrieve a specific task by ID  
**Authentication**: None

**URL Parameters**:
```
id (integer, required): Task ID
```

**Response** (Status: 200 OK):
```json
{
  "id": 1,
  "title": "Learn Docker",
  "description": "Study Docker containerization concepts",
  "status": "pending",
  "created_at": "2026-02-16T10:23:45.123456"
}
```

**Error Responses**:
```json
// 404 Not Found
{
  "error": "Task not found"
}
```

**Example Requests**:

PowerShell:
```powershell
Invoke-RestMethod -Uri http://localhost:5000/tasks/1
```

curl/bash:
```bash
curl http://localhost:5000/tasks/1
```

---

### 4. Update Task

**Endpoint**: `PUT /tasks/<id>`  
**Description**: Update task fields (supports partial updates)  
**Authentication**: None

**URL Parameters**:
```
id (integer, required): Task ID
```

**Request Body** (all fields optional):
```json
{
  "title": "Updated title",
  "description": "Updated description",
  "status": "completed"
}
```

**Field Descriptions**:
- `title`: New task title (leave out if not changing)
- `description`: New task description (leave out if not changing)
- `status`: Task status - must be "pending" or "completed"

**Response** (Status: 200 OK):
```json
{
  "id": 1,
  "title": "Updated title",
  "description": "Updated description",
  "status": "completed",
  "created_at": "2026-02-16T10:23:45.123456"
}
```

**Error Responses**:
```json
// 404 Not Found
{
  "error": "Task not found"
}

// 400 Bad Request - Invalid status
{
  "error": "Invalid status"
}
```

**Example Requests**:

PowerShell:
```powershell
# Update only status
Invoke-RestMethod -Method PUT `
  -Uri http://localhost:5000/tasks/1 `
  -ContentType "application/json" `
  -Body '{"status":"completed"}'

# Update multiple fields
$updates = @{
    title = "Updated Title"
    status = "completed"
} | ConvertTo-Json

Invoke-RestMethod -Method PUT `
  -Uri http://localhost:5000/tasks/1 `
  -ContentType "application/json" `
  -Body $updates
```

curl/bash:
```bash
# Update only status
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"completed"}'

# Update multiple fields
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Title",
    "status": "completed"
  }'
```

---

### 5. Delete Task

**Endpoint**: `DELETE /tasks/<id>`  
**Description**: Delete a task  
**Authentication**: None

**URL Parameters**:
```
id (integer, required): Task ID
```

**Response** (Status: 204 No Content):
```
(No response body)
```

**Error Responses**:
```json
// 404 Not Found
{
  "error": "Task not found"
}
```

**Example Requests**:

PowerShell:
```powershell
Invoke-RestMethod -Method DELETE -Uri http://localhost:5000/tasks/1
```

curl/bash:
```bash
curl -X DELETE http://localhost:5000/tasks/1
```

---

## 💾 Database Schema

### Task Model

**Table**: `task`

**Columns**:

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | Integer | PRIMARY KEY, Auto-increment | Unique task identifier |
| `title` | String(100) | NOT NULL | Task title/name |
| `description` | String(200) | NULLABLE | Detailed task description |
| `status` | String(20) | DEFAULT: 'pending' | Current status (pending/completed) |
| `created_at` | DateTime | DEFAULT: UTC Now | Task creation timestamp |

**SQLAlchemy Model** (`models.py`):
```python
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }
```

**Status Values**:
- `pending`: Task is not yet started
- `completed`: Task has been finished

### Database Files

**Development**: `instance/tasks.db` (SQLite file)  
**Testing**: In-memory SQLite (`:memory:`)  
**Production**: Connect to PostgreSQL via environment variable

---

## 🚀 Deployment Process

### Option 1: Local Development

```bash
# Setup
git clone <repo-url>
cd Devops-labs
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Run
python app.py

# Test
pytest -v --cov=app
```

### Option 2: Docker Compose (Recommended)

```bash
# Clone repository
git clone <repo-url>
cd Devops-labs

# Build and run
docker-compose up --build

# In another terminal, run tests
docker-compose exec api pytest -v

# Stop services
docker-compose down
```

### Option 3: Docker Production Deployment

**Build Image**:
```bash
docker build -t task-api:v1.0.0 .
```

**Run Container**:
```bash
docker run -d \
  --name task-api \
  -p 5000:5000 \
  -e FLASK_ENV=production \
  task-api:v1.0.0
```

**Push to Registry** (e.g., Docker Hub):
```bash
docker tag task-api:v1.0.0 yourusername/task-api:v1.0.0
docker push yourusername/task-api:v1.0.0
```

**Deploy to Kubernetes**:
```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: task-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: task-api
  template:
    metadata:
      labels:
        app: task-api
    spec:
      containers:
      - name: api
        image: yourusername/task-api:v1.0.0
        ports:
        - containerPort: 5000
        env:
        - name: FLASK_ENV
          value: production
---
apiVersion: v1
kind: Service
metadata:
  name: task-api-service
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 5000
  selector:
    app: task-api
```

Deploy:
```bash
kubectl apply -f deployment.yaml
```

---

## 📊 Monitoring & Troubleshooting

### Logging

**Log Levels**:
- `DEBUG`: Detailed information for debugging
- `INFO`: General informational messages
- `WARNING`: Warning messages for potentially harmful situations
- `ERROR`: Error messages for serious problems
- `CRITICAL`: Critical errors that may cause shutdown

**View Application Logs**:

Local:
```bash
# Console output automatically shows logs
python app.py
```

Docker:
```bash
docker-compose logs -f api
```

Kubernetes:
```bash
kubectl logs -f deployment/task-api
```

**Example Log Output**:
```
2026-02-16 10:23:45,123 - app.routes - INFO - Request: POST http://localhost:5000/tasks
2026-02-16 10:23:45,124 - app.routes - INFO - Creating new task
2026-02-16 10:23:45,145 - app.routes - INFO - Response: 201
```

### Health Checks

**Docker Health Check**:
```bash
curl http://localhost:5000/tasks
```

**Kubernetes Health Probe**:
```yaml
livenessProbe:
  httpGet:
    path: /tasks
    port: 5000
  initialDelaySeconds: 5
  periodSeconds: 10
```

### Performance Monitoring

**Test API Performance** (Apache Bench):
```bash
# Benchmark 100 requests, 10 concurrent
ab -n 100 -c 10 http://localhost:5000/tasks
```

**View Test Coverage**:
```bash
pytest --cov=app --cov-report=html
# Open htmlcov/index.html in browser
```

### Common Issues & Resolution

**Issue**: Database file not found for `instance/tasks.db`
```
Resolution: Run `python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all()"`
```

**Issue**: Port 5000 already in use
```
Resolution: 
  # Kill process on port 5000
  lsof -ti:5000 | xargs kill -9  # Linux/Mac
  netstat -ano | findstr :5000   # Windows, then taskkill /PID <PID> /F
```

**Issue**: Tests fail with "No module named 'app'"
```
Resolution: Ensure you're in the project root directory and virtual environment is activated
```

**Issue**: Docker container exits immediately
```
Resolution: Check logs with `docker logs <container-id>`
           Ensure Dockerfile and app.py are correct
```

---

## 🔒 Security Considerations

### Current Security Measures
- ✅ Input validation (title required, status validated)
- ✅ Error handling (no stack traces exposed to clients)
- ✅ Database transaction support (prevents partial updates)
- ✅ HTTPS-ready (application agnostic to HTTP vs HTTPS)

### Recommended Security Enhancements

**1. Authentication & Authorization**
```python
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    # Implement user authentication
    access_token = create_access_token(identity='user_id')
    return jsonify(access_token=access_token)

@bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    # Protected endpoint
    pass
```

**2. Input Sanitization**
```python
from bleach import clean

def sanitize_input(text):
    return clean(text, strip=True, tags=[])
```

**3. Rate Limiting**
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@bp.route('/tasks', methods=['POST'])
@limiter.limit("5 per minute")
def create_task():
    pass
```

**4. CORS Configuration**
```python
from flask_cors import CORS

CORS(app, resources={r"/tasks/*": {"origins": ["https://example.com"]}})
```

---

## ⚡ Performance Optimization

### Current Optimizations
- ✅ Lightweight Flask framework
- ✅ Efficient SQLAlchemy queries
- ✅ In-memory test database
- ✅ Multi-stage Docker builds

### Recommended Optimizations

**1. Database Indexing**
```python
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    status = db.Column(db.String(20), default='pending', index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
```

**2. Pagination**
```python
@bp.route('/tasks', methods=['GET'])
def get_tasks():
    page = request.args.get('page', 1, type=int)
    tasks = Task.query.paginate(page=page, per_page=10)
    return jsonify({
        'tasks': [task.to_dict() for task in tasks.items],
        'total': tasks.total,
        'pages': tasks.pages
    })
```

**3. Caching**
```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@bp.route('/tasks', methods=['GET'])
@cache.cached(timeout=300)
def get_tasks():
    pass
```

**4. Connection Pooling**
```python
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 10,
    'pool_recycle': 3600,
    'pool_pre_ping': True,
}
```

---

## 📚 Additional Resources

### Documentation
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [pytest Documentation](https://docs.pytest.org/)
- [Docker Documentation](https://docs.docker.com/)
- [REST API Best Practices](https://restfulapi.net/)

### Tools & Services
- Postman: API testing (https://www.postman.com/)
- GitHub Actions: CI/CD (https://github.com/features/actions)
- Docker Hub: Image registry (https://hub.docker.com/)

### Recommended Reading
- "Test Driven Development" by Kent Beck
- "The Twelve-Factor App" by Heroku
- "Site Reliability Engineering" by Google

---

## 📞 Support & Feedback

For issues, questions, or suggestions:
1. Check this documentation
2. Review [README.md](README.md) and sprint documentation
3. Check test files for usage examples
4. Create GitHub issue with details

---

**Documentation Version**: 2.0  
**Last Updated**: February 2026  
**Maintained by**: Development Team  
**Status**: ✅ Production Ready
