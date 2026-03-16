from fastapi import FastAPI
from app.routers import employee

app = FastAPI(title="Salary Management")

app.include_router(employee.router)
