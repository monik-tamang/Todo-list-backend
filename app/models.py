from sqlalchemy import Column, String, Boolean, TIMESTAMP, text, UUID, ForeignKey, Enum
from app.database import Base
from sqlalchemy.orm import relationship
from app.schema import Title

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID, primary_key=True, nullable=False, unique=True, server_default=text('gen_random_uuid()'))
    name = Column(String, nullable=False)
    completed = Column(Boolean, server_default='False', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    completed_at = Column(TIMESTAMP(timezone=True), server_default=None, nullable=True)
    priority = Column(String, server_default='None', nullable=False)
    title = Column(Enum(Title, name="title_enum", create_type=False), nullable=False, server_default=Title.Home.value)
    user_id = Column(UUID, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    user = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, nullable=False, unique=True, server_default=text('gen_random_uuid()'))
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)