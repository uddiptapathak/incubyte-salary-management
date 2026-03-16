from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate


def create(db: Session, payload: EmployeeCreate) -> Employee:
    employee = Employee(**payload.model_dump())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


def get_by_id(db: Session, employee_id: int) -> Employee | None:
    return db.query(Employee).filter(Employee.id == employee_id).first()
