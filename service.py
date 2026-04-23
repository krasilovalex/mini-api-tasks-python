from typing import List
from fastapi import HTTPException
from schemas import CreateTask, Task


tasks_db: List[Task] = []
current_id: int = 1


def create_task(task_in: CreateTask) -> Task:
    global current_id

    new_task = Task(id=current_id, **task_in.model_dump())
    tasks_db.append(new_task)


    current_id += 1
    return new_task


def get_all_tasks() -> List[Task]:
    return tasks_db


def get_task_by_id(task_id: int) -> Task:
    for task in tasks_db:
        if task.id == task_id:
            return task
        
    raise HTTPException(status_code=404, detail="Задача не найдена")