from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.employee import CountrySalaryMetrics
from app.services import metrics as metrics_service

router = APIRouter(prefix="/salary-metrics", tags=["metrics"])


@router.get("/country/{country}", response_model=CountrySalaryMetrics)
def get_country_metrics(country: str, db: Session = Depends(get_db)):
    metrics = metrics_service.get_country_metrics(db, country)
    if not metrics:
        raise HTTPException(status_code=404, detail="No employees found for this country")
    return metrics
