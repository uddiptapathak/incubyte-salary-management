from sqlalchemy import func
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
    employee = get_by_id(db, employee_id)
    if not employee:
        return False
    db.delete(employee)
    db.commit()
    return True


def get_avg_salary_by_job_title(db: Session, job_title: str) -> float | None:
    return db.query(func.avg(Employee.salary)).filter(Employee.job_title == job_title).scalar()


def get_salary_stats_by_country(db: Session, country: str) -> dict:
    result = db.query(
        func.min(Employee.salary),
        func.max(Employee.salary),
        func.avg(Employee.salary),
    ).filter(Employee.country == country).one()
    return {"min_salary": result[0], "max_salary": result[1], "average_salary": result[2]}


def update(db: Session, employee_id: int, payload: EmployeeCreate) -> Employee | None:
    employee = get_by_id(db, employee_id)
    if not employee:
        return None
    for key, value in payload.model_dump().items():
        setattr(employee, key, value)
    db.commit()
    db.refresh(employee)
    return employee
