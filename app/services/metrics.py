from sqlalchemy.orm import Session

from app.repositories import employee as employee_repo
from app.schemas.employee import CountrySalaryMetrics


def get_country_metrics(db: Session, country: str) -> CountrySalaryMetrics | None:
    stats = employee_repo.get_salary_stats_by_country(db, country)
    if stats["min_salary"] is None:
        return None
    return CountrySalaryMetrics(**stats)
