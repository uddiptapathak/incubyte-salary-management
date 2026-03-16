# Incubyte Salary Management API

A FastAPI application for managing employees, calculating salary deductions, and providing salary metrics.

## Tech Stack

- **Python 3.12** with **FastAPI**
- **SQLAlchemy** ORM with **SQLite**
- **Pydantic** for request/response validation
- **pytest** + **httpx** for async testing

## Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API docs available at `http://localhost:8000/docs`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/employees` | Create employee |
| GET | `/employees` | List all employees |
| GET | `/employees/{id}` | Get employee by ID |
| PUT | `/employees/{id}` | Update employee |
| DELETE | `/employees/{id}` | Delete employee |
| GET | `/employees/{id}/salary` | Get salary breakdown |
| GET | `/salary-metrics/country/{country}` | Min, max, avg salary by country |
| GET | `/salary-metrics/job-title/{title}` | Average salary by job title |

## Salary Deduction Rules

| Country | TDS Rate |
|---------|----------|
| India | 10% |
| United States | 12% |
| All others | 0% |

## Running Tests

```bash
pytest -v
```

## Project Structure

```
app/
├── main.py              # FastAPI app entry point
├── database.py          # SQLAlchemy database config
├── models/              # ORM models
├── schemas/             # Pydantic schemas
├── repositories/        # Data access layer
├── services/            # Business logic layer
└── routers/             # API route handlers
tests/
├── conftest.py          # Test fixtures (in-memory SQLite)
├── test_employee_crud.py
├── test_salary_calculation.py
└── test_salary_metrics.py
```

## Implementation Details

- Followed strict **TDD workflow** (RED → GREEN → Refactor) — visible in commit history
- Layered architecture: Router → Service → Repository → Model
- Input validation: salary must be positive, all fields required
- Consistent error responses with standard `ErrorResponse` schema
- **AI tools used**: Claude Code (Anthropic) for scaffolding, test generation, code review, and refactoring guidance
