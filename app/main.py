from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine, get_db
from typing import Union

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
)

@app.exception_handler(HTTPException)
async def custom_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content={"error": "There is no task at that id"},
    )

@app.post("/v1/tasks", status_code=201, response_model=Union[schemas.TaskIDResponse, schemas.TaskListResponse])
def create_tasks(tasks: Union[schemas.BulkListResponse, schemas.TaskCreateAndUpdate], db: Session = Depends(get_db)):
        if isinstance(tasks, schemas.BulkListResponse):
            created_tasks = crud.bulk_create_tasks(db, tasks)
            return {"tasks": created_tasks}
        elif isinstance(tasks, schemas.TaskCreateAndUpdate):
            created_task = crud.create_task(db, tasks)
            return {"id": created_task.id}

@app.get("/v1/tasks", response_model=schemas.TaskListGetResponse)
def get_tasks(db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    return {"tasks": tasks}

@app.get("/v1/tasks/{task_id}", response_model=schemas.Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail={"error": "There is no task at that id"})
    return task

@app.delete("/v1/tasks/{task_id}", status_code=204, response_model=None)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    crud.delete_task(db, task_id)
    return None

@app.delete("/v1/tasks", status_code=204, response_model=None)
def delete_tasks(tasks: schemas.TaskListResponse, db: Session = Depends(get_db)):
    task_ids = [task.id for task in tasks.tasks]
    crud.bulk_delete_tasks(db, task_ids)
    return None

@app.put("/v1/tasks/{task_id}", status_code=204, response_model=None)
def update_task(task_id: int, task_update: schemas.TaskCreateAndUpdate, db: Session = Depends(get_db)):
    updated_task = crud.update_task(db, task_id, task_update)
    if updated_task is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "There is no task at that id"}
        )
    return None

