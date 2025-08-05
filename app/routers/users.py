from fastapi import status, HTTPException, Depends, APIRouter
from app import models
from app.utils import hash
from app.database import get_session
from app.schema import UserCreate, UserResponse
from uuid import UUID


router = APIRouter(prefix="/user", tags=['Users'])


# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
# def create_user(user: UserCreate, session = Depends(get_session)):

#     hashed_password = hash(user.password)
#     user.password = hashed_password
#     new_user = models.User(**user.model_dump())
#     session.add(new_user)
#     session.commit()
#     session.refresh(new_user)

#     return new_user


@router.get("/{id}", response_model=UserResponse)
def get_user(id:UUID, session = Depends(get_session)):
    user = session.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} doesnot exist")

    return user
