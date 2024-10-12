from sqlalchemy.orm import Session
from . import models, schemas

def create_task(db: Session, task: schemas.Task):
    db_task = models.Task(title=task.title, is_completed = task.is_completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session):
    return db.query(models.Task).all()

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def delete_task(db: Session, task_id: int):
    delete_task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if delete_task:
        db.delete(delete_task) 
        db.commit()

def update_task(db: Session, task_id: int, task_update: schemas.Task):
    update_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if update_task is None:
        return None
    update_task.title = task_update.title
    update_task.is_completed = task_update.is_completed

    db.commit()
    db.refresh(update_task)
    return update_task

def bulk_create_tasks(db: Session, tasks: schemas.TaskListResponse):
    created_tasks = []  
    for task in tasks.tasks:
        db_task = models.Task(title=task.title, is_completed=task.is_completed)
        db.add(db_task)
        created_tasks.append(db_task)
    db.commit()
    return [{"id": task.id} for task in created_tasks]

def bulk_delete_tasks(db: Session, task_ids: list[int]):
    for task_id in task_ids:
        task = db.query(models.Task).filter(models.Task.id == task_id).first()
        if task:
            db.delete(task)
    db.commit()