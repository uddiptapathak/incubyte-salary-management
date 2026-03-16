import pytest


@pytest.mark.asyncio
async def test_salary_calculation_india_10_percent_tds(client):
    payload = {
        "full_name": "Raj Kumar",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 50000.0,
    }
    create_response = await client.post("/employees", json=payload)
    employee_id = create_response.json()["id"]

    response = await client.get(f"/employees/{employee_id}/salary")

    assert response.status_code == 200
    data = response.json()
    assert data["gross_salary"] == 50000.0
    assert data["deductions"] == 5000.0
    assert data["net_salary"] == 45000.0


@pytest.mark.asyncio
async def test_salary_calculation_us_12_percent_tds(client):
    payload = {
        "full_name": "John Smith",
        "job_title": "Data Scientist",
        "country": "United States",
        "salary": 80000.0,
    }
    create_response = await client.post("/employees", json=payload)
    employee_id = create_response.json()["id"]

    response = await client.get(f"/employees/{employee_id}/salary")

    assert response.status_code == 200
    data = response.json()
    assert data["gross_salary"] == 80000.0
    assert data["deductions"] == 9600.0
    assert data["net_salary"] == 70400.0
