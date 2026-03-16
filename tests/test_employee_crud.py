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


@pytest.mark.asyncio
async def test_create_employee_missing_full_name_returns_422(client):
    payload = {
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 50000.0,
    }
    response = await client.post("/employees", json=payload)

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_employee_by_id_returns_200(client):
    payload = {
        "full_name": "Jane Doe",
        "job_title": "Data Analyst",
        "country": "United States",
        "salary": 70000.0,
    }
    create_response = await client.post("/employees", json=payload)
    employee_id = create_response.json()["id"]

    response = await client.get(f"/employees/{employee_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == employee_id
    assert data["full_name"] == payload["full_name"]
    assert data["job_title"] == payload["job_title"]
    assert data["country"] == payload["country"]
    assert data["salary"] == payload["salary"]


@pytest.mark.asyncio
async def test_get_all_employees_returns_list(client):
    for name in ["Alice", "Bob"]:
        await client.post("/employees", json={
            "full_name": name,
            "job_title": "Engineer",
            "country": "India",
            "salary": 40000.0,
        })

    response = await client.get("/employees")

    assert response.status_code == 200
    assert len(response.json()) == 2


@pytest.mark.asyncio
async def test_update_employee_returns_200_with_updated_data(client):
    payload = {
        "full_name": "John Doe",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 50000.0,
    }
    create_response = await client.post("/employees", json=payload)
    employee_id = create_response.json()["id"]

    updated_payload = {
        "full_name": "John Doe",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 60000.0,
    }
    response = await client.put(f"/employees/{employee_id}", json=updated_payload)

    assert response.status_code == 200
    data = response.json()
    assert data["salary"] == 60000.0
    assert data["full_name"] == payload["full_name"]
    assert data["job_title"] == payload["job_title"]
    assert data["country"] == payload["country"]


@pytest.mark.asyncio
async def test_update_nonexistent_employee_returns_404(client):
    payload = {
        "full_name": "Ghost User",
        "job_title": "Engineer",
        "country": "India",
        "salary": 50000.0,
    }
    response = await client.put("/employees/9999", json=payload)

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_delete_employee_returns_204(client):
    payload = {
        "full_name": "John Doe",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 50000.0,
    }
    create_response = await client.post("/employees", json=payload)
    employee_id = create_response.json()["id"]

    delete_response = await client.delete(f"/employees/{employee_id}")
    assert delete_response.status_code == 204

    get_response = await client.get(f"/employees/{employee_id}")
    assert get_response.status_code == 404


@pytest.mark.asyncio
async def test_delete_nonexistent_employee_returns_404(client):
    response = await client.delete("/employees/9999")

    assert response.status_code == 404
