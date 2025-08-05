from fastapi import Depends, Query, HTTPException, status
from app.database import get_session
from app.schema import TaskListResponse, TaskResponse, TaskType, MessageResponse, Title
from app.models import Task
from sqlalchemy import func
from datetime import datetime

def get_tasks(session, task_type, task_title, limit, offset) -> TaskListResponse:

    query = session.query(Task)

    if task_type == TaskType.today:
        query = query.filter(func.date(Task.created_at) == datetime.now().date())
    elif task_type == TaskType.completed:
        query = query.filter(Task.completed == True)
    elif task_type == TaskType.remaining:
        query = query.filter(Task.completed == False)
    
    number_of_tasks = query.count()
    tasks = query.order_by(Task.completed,Task.created_at.desc()).offset(offset).limit(limit).all()

    return {
        "total": number_of_tasks, 
        "limit": limit,
        "offset":offset, 
        "task_type":task_type, 
        "tasks":tasks
    }

def create_task(task_schema, session, current_user) -> MessageResponse:
    new_task = Task(name=task_schema.name, user_id=current_user.id)
    session.add(new_task)
    session.commit()

    return  "Task created successfully"

def update_task(id, task_schema, session) -> TaskResponse:
    task = session.query(Task).filter(Task.id == id)
    task_data = task.first()

    if task_schema.completed == True:
        task_schema.completed_at = datetime.now()
    else:
        task_schema.completed_at = None

    if task_data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"task with id: {id} does not exist")

    task.update(task_schema.model_dump(exclude_unset=True), synchronize_session='fetch')
    session.commit()

    return task_data

def delete_task(id, session):
    task = session.query(Task).filter(Task.id == id)
    task_data = task.first()

    if task_data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"task with id: {id} does not exist")
    
    task.delete(synchronize_session = False)
    session.commit()
