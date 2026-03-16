from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.repositories import employee as employee_repo
from app.schemas.employee import EmployeeCreate


def create_employee(db: Session, payload: EmployeeCreate) -> Employee:
    """Create a new employee record."""
    return employee_repo.create(db, payload)


def get_employee(db: Session, employee_id: int) -> Employee | None:
    """Retrieve an employee by ID, or None if not found."""
    return employee_repo.get_by_id(db, employee_id)


def get_all_employees(db: Session) -> list[Employee]:
    """Retrieve all employee records."""
    return employee_repo.get_all(db)


def delete_employee(db: Session, employee_id: int) -> bool:
    """Delete an employee by ID. Returns True if deleted, False if not found."""
    return employee_repo.delete(db, employee_id)


def update_employee(db: Session, employee_id: int, payload: EmployeeCreate) -> Employee | None:
    """Update an employee by ID. Returns updated employee, or None if not found."""
    return employee_repo.update(db, employee_id, payload)
