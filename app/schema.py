from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum
from uuid import UUID


class TaskType(str, Enum):
   all = "all"
   today = "today"
   completed = "completed"
   remaining = "remaining"
   project = "project"
   home = "home"
   exercise = "exercise"
   work = "work"
   study = "study"
   others = "others"

class PriorityType(str, Enum):
   none = "None"
   low = "Low"
   medium = "Medium"
   high = "High"


class Title(str, Enum):
   Project = "Project"
   Home = "Home"
   Exercise = "Exercise"
   Work = "Work"
   Study = "Study"
   Others = "Others"


class CreateTask(BaseModel):
   name: str
   
   duplicate_status: Optional[bool] = True


class Pagination(BaseModel):
   limit: int
   offset: int
   total: int

class TaskResponse(BaseModel):
   id: UUID
   user_id: UUID
   name: str
   completed: Optional[bool] = False
   created_at: datetime
   completed_at: Optional[datetime] = None
   priority: str
   title: str


class GetResponse():
   completed: bool


class UpdateTask(BaseModel):
   name: Optional[str] = None
   completed: Optional[bool] = None
   completed_at: Optional[datetime] = None
   priority: Optional[str] = None
   title: Optional[str] = None


class MessageResponse(BaseModel):
   message: str
   status: bool


class TaskListResponse(Pagination):
   tasks: List[TaskResponse]
   task_type: TaskType


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    created_at: datetime


class UserCreate(BaseModel):
    email: EmailStr 
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[UUID]
