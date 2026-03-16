from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.repositories import employee as employee_repo
from app.schemas.employee import EmployeeCreate


def create_employee(db: Session, payload: EmployeeCreate) -> Employee:
    return employee_repo.create(db, payload)


def get_employee(db: Session, employee_id: int) -> Employee | None:
    return employee_repo.get_by_id(db, employee_id)


def get_all_employees(db: Session) -> list[Employee]:
    return employee_repo.get_all(db)


def delete_employee(db: Session, employee_id: int) -> bool:
    return employee_repo.delete(db, employee_id)


def update_employee(db: Session, employee_id: int, payload: EmployeeCreate) -> Employee | None:
    return employee_repo.update(db, employee_id, payload)
