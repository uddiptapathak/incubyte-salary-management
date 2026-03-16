import pytest


@pytest.mark.asyncio
async def test_salary_metrics_by_country(client):
    for salary in [40000.0, 50000.0, 60000.0]:
        await client.post("/employees", json={
            "full_name": "Test Employee",
            "job_title": "Engineer",
            "country": "India",
            "salary": salary,
        })

    response = await client.get("/salary-metrics/country/India")

    assert response.status_code == 200
    data = response.json()
    assert data["min_salary"] == 40000.0
    assert data["max_salary"] == 60000.0
    assert data["average_salary"] == 50000.0


@pytest.mark.asyncio
async def test_salary_metrics_by_country_no_employees_returns_404(client):
    response = await client.get("/salary-metrics/country/Atlantis")

    assert response.status_code == 404
