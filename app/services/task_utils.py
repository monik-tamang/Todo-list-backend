from app.machine_learning.duplicate_detection import is_duplicate
from app.models import Task
from sqlalchemy import or_, func
from datetime import datetime

def duplicate_checker(session, new_task: str):
    tasks = session.query(Task.name).filter(or_(Task.completed == False, func.date(Task.created_at) == datetime.now().date())).all()

    tasks = [(task[0]) for task in tasks]

    result = is_duplicate(new_task, tasks)

    return result
