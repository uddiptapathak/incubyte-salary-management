from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.employee import CountrySalaryMetrics, ErrorResponse, JobTitleSalaryMetrics
from app.services import metrics as metrics_service

router = APIRouter(prefix="/salary-metrics", tags=["metrics"])


@router.get("/country/{country}", response_model=CountrySalaryMetrics, responses={404: {"model": ErrorResponse}})
def get_country_metrics(country: str, db: Session = Depends(get_db)):
    metrics = metrics_service.get_country_metrics(db, country)
    if not metrics:
        raise HTTPException(status_code=404, detail="No employees found for this country")
    return metrics


@router.get("/job-title/{job_title}", response_model=JobTitleSalaryMetrics, responses={404: {"model": ErrorResponse}})
def get_job_title_metrics(job_title: str, db: Session = Depends(get_db)):
    metrics = metrics_service.get_job_title_metrics(db, job_title)
    if not metrics:
        raise HTTPException(status_code=404, detail="No employees found for this job title")
    return metrics
