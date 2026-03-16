from pydantic import BaseModel, Field


class EmployeeCreate(BaseModel):
    full_name: str
    job_title: str
    country: str
    salary: float = Field(gt=0)


class EmployeeResponse(EmployeeCreate):
    id: int

    model_config = {"from_attributes": True}


class SalaryBreakdown(BaseModel):
    gross_salary: float
    deductions: float
    net_salary: float


class CountrySalaryMetrics(BaseModel):
    min_salary: float
    max_salary: float
    average_salary: float


class JobTitleSalaryMetrics(BaseModel):
    job_title: str
    average_salary: float


class ErrorResponse(BaseModel):
    detail: str
