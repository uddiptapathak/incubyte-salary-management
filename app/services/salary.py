from app.models.employee import Employee
from app.schemas.employee import SalaryBreakdown

TDS_RATES: dict[str, float] = {
    "India": 0.10,
    "United States": 0.12,
}


def calculate_salary(employee: Employee) -> SalaryBreakdown:
    gross = employee.salary
    deductions = gross * TDS_RATES.get(employee.country, 0.0)
    return SalaryBreakdown(
        gross_salary=gross,
        deductions=deductions,
        net_salary=gross - deductions,
    )
