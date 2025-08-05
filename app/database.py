from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings


database_url = f"postgresql+psycopg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
Base = declarative_base()

def get_session():
    with SessionLocal() as session:
        yield session
