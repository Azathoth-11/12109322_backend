from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    id: int
    title: str
    is_completed: bool = False

    class config:
        from_attribute = True

class TaskListGetResponse(BaseModel):
    tasks: List[Task]

class TaskCreateAndUpdate(BaseModel):
    title: str
    is_completed: bool = False

class TaskIDResponse(BaseModel):
    id: int

class TaskListResponse(BaseModel):
    tasks: List[TaskIDResponse]

class BulkListResponse(BaseModel):
    tasks: List[TaskCreateAndUpdate]

