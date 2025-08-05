from fastapi import FastAPI
from app.routers import tasks, users, auth
from app.database import engine
from app import models
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(engine)

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(auth.router)
app.include_router(tasks.router)




