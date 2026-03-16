import pytest


@pytest.mark.asyncio
async def test_create_employee_returns_201_with_employee_data(client):
    payload = {
        "full_name": "John Doe",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 50000.0,
    }
    response = await client.post("/employees", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["full_name"] == payload["full_name"]
    assert data["job_title"] == payload["job_title"]
    assert data["country"] == payload["country"]
    assert data["salary"] == payload["salary"]
    assert "id" in data
