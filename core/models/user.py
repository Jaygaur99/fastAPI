from sqlalchemy import Column, Integer, String
from services.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(500))

    todos = relationship("Todo", back_populates="user")

    def __str__(self) -> str:
        return f"{self.email}"

    def __eq__(self, other: object) -> bool:
        if (isinstance(other, User)):
            return self.id == other.id
        return False
