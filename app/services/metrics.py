from sqlalchemy.orm import Session

from app.repositories import employee as employee_repo
from app.schemas.employee import CountrySalaryMetrics, JobTitleSalaryMetrics


def get_job_title_metrics(db: Session, job_title: str) -> JobTitleSalaryMetrics | None:
    """Get average salary for a given job title. Returns None if no employees found."""
    avg = employee_repo.get_avg_salary_by_job_title(db, job_title)
    if avg is None:
        return None
    return JobTitleSalaryMetrics(job_title=job_title, average_salary=avg)


def get_country_metrics(db: Session, country: str) -> CountrySalaryMetrics | None:
    """Get min, max, and average salary for a given country. Returns None if no employees found."""
    stats = employee_repo.get_salary_stats_by_country(db, country)
    if stats["min_salary"] is None:
        return None
    return CountrySalaryMetrics(**stats)
