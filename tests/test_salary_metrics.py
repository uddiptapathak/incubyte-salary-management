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


@pytest.mark.asyncio
async def test_average_salary_by_job_title(client):
    for salary in [50000.0, 60000.0, 70000.0]:
        await client.post("/employees", json={
            "full_name": "Test Employee",
            "job_title": "Software Engineer",
            "country": "India",
            "salary": salary,
        })
    await client.post("/employees", json={
        "full_name": "Test Designer",
        "job_title": "Designer",
        "country": "India",
        "salary": 45000.0,
    })

    response = await client.get("/salary-metrics/job-title/Software Engineer")

    assert response.status_code == 200
    data = response.json()
    assert data["job_title"] == "Software Engineer"
    assert data["average_salary"] == 60000.0


@pytest.mark.asyncio
async def test_average_salary_by_job_title_no_employees_returns_404(client):
    response = await client.get("/salary-metrics/job-title/Astronaut")

    assert response.status_code == 404
