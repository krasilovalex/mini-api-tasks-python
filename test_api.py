import pytest
from fastapi.testclient import TestClient
from main import app
import service

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_db():
    service.tasks_db.clear()
    service.current_id = 1
    yield


def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Решить тесовое задание", "description": "Написать эндпоитны для мини-таска", "status": "new"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Решить тесовое задание"
    assert data["status"] == "new"



def test_get_tasks_empty():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []

def test_get_tasks_with_data():
    client.post("/tasks", json={"title": "Написать скрипт", "status": "in_progress"})


    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Написать скрипт"

def test_get_task_by_id_success():
    client.post("/tasks", json={"title": "Решить задачу", "status": "done"})

    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_get_task_by_id_not_found():
    response = client.get("/tasks/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Задача не найдена"

def test_create_task_validation_error():
    response = client.post(
        "/tasks",
        json={"description": "Нет названия", "status": "Невалидный статус"}
    )
    assert response.status_code == 422