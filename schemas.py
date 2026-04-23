from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class TaskStatus(str, Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"


class CreateTask(BaseModel):
    title: str = Field(..., description="Название задачи")
    description: Optional[str] = Field(None, description="Описание задачи")
    status: TaskStatus = Field(..., description="Статус задачи")


class Task(CreateTask):
    id: int