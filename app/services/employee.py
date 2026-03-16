from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.repositories import employee as employee_repo
from app.schemas.employee import EmployeeCreate


def create_employee(db: Session, payload: EmployeeCreate) -> Employee:
    return employee_repo.create(db, payload)
