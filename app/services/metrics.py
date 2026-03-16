from sqlalchemy.orm import Session

from app.repositories import employee as employee_repo
from app.schemas.employee import CountrySalaryMetrics, JobTitleSalaryMetrics


def get_job_title_metrics(db: Session, job_title: str) -> JobTitleSalaryMetrics | None:
    avg = employee_repo.get_avg_salary_by_job_title(db, job_title)
    if avg is None:
        return None
    return JobTitleSalaryMetrics(job_title=job_title, average_salary=avg)


def get_country_metrics(db: Session, country: str) -> CountrySalaryMetrics | None:
    stats = employee_repo.get_salary_stats_by_country(db, country)
    if stats["min_salary"] is None:
        return None
    return CountrySalaryMetrics(**stats)
