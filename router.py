from fastapi import APIRouter
from typing import List
import service
from schemas import CreateTask, Task



router = APIRouter(prefix="/tasks", tags=["Tasks"])

# POST /tasks

@router.post("", response_model=Task, status_code=201)
def create_task_endpoint(task: CreateTask):
    return service.create_task(task)


# GET /tasks
@router.get("", response_model=List[Task])
def get_tasks_endpoint():
    return service.get_all_tasks()

# GET /tasks/:id
@router.get("/{task_id}", response_model=Task)
def get_tasks_endpoint(task_id: int):
    return service.get_task_by_id(task_id)
    