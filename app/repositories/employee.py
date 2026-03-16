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


def get_all(db: Session) -> list[Employee]:
    return db.query(Employee).all()


def delete(db: Session, employee_id: int) -> bool:
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return False
    db.delete(employee)
    db.commit()
    return True


def update(db: Session, employee_id: int, payload: EmployeeCreate) -> Employee | None:
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return None
    for key, value in payload.model_dump().items():
        setattr(employee, key, value)
    db.commit()
    db.refresh(employee)
    return employee
