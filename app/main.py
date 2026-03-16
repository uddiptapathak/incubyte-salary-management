from fastapi import FastAPI
from app.routers import employee, metrics

app = FastAPI(title="Salary Management")

app.include_router(employee.router)
app.include_router(metrics.router)
