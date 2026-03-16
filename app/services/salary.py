from app.models.employee import Employee
from app.schemas.employee import SalaryBreakdown


def calculate_salary(employee: Employee) -> SalaryBreakdown:
    gross = employee.salary
    if employee.country == "India":
        deductions = gross * 0.10
    elif employee.country == "United States":
        deductions = gross * 0.12
    return SalaryBreakdown(
        gross_salary=gross,
        deductions=deductions,
        net_salary=gross - deductions,
    )
