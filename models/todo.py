from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    description = Column(String(100))
    completed = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="todos")
