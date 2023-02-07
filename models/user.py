from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))

    todos = relationship("Todo", back_populates="user")
