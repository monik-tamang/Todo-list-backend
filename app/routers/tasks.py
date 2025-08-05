from fastapi import APIRouter, Response, status, HTTPException, Query, Depends
from app.schema import CreateTask, TaskResponse, UpdateTask, TaskType, TaskListResponse, MessageResponse, Title
from app.database import get_session
from uuid import UUID
from app.crud import tasks
from app.services.task_utils import duplicate_checker
from app import oauth2


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("", response_model=TaskListResponse)
def get_tasks(
    session = Depends(get_session),
    current_user: int = Depends(oauth2.get_current_user),
    task_type: TaskType = TaskType.all,
    task_title: Title = Title.Study,
    limit: int = Query(10, ge=1, le=10),
    offset: int = Query(0, ge=0),
):
    data = tasks.get_tasks(session, task_type, task_title, limit, offset)
    
    return data

@router.post("", status_code=status.HTTP_201_CREATED, response_model=MessageResponse)
def create_task(task_schema: CreateTask, session = Depends(get_session), current_user: int = Depends(oauth2.get_current_user)):
    status = False

    if task_schema.duplicate_status == True:
        result = duplicate_checker(session, task_schema.name)
        status = result[0]

    if status == True:
        message = f"Duplicate task detected: {result[1]}"
    else:
        message = tasks.create_task(task_schema, session, current_user)

    return {"message":message, "status":status}

@router.put("/{id}", response_model= TaskResponse)
def update_task(id: UUID, task_scheme: UpdateTask, session = Depends(get_session), current_user: int = Depends(oauth2.get_current_user)):
    updated_task = tasks.update_task(id, task_scheme, session)

    return updated_task

@router.delete("/{id}")
def delete_task(id: UUID, session = Depends(get_session), current_user: int = Depends(oauth2.get_current_user)):
    tasks.delete_task(id, session)

    return Response(status_code=status.HTTP_204_NO_CONTENT)