from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from services.database import Base


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    description = Column(String(100))
    completed = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="todos")

    def __str__(self) -> str:
        return f"{self.name} - {self.description}"

    def __eq__(self, other: object) -> bool:
        if (isinstance(other, Todo)):
            return self.id == other.id
        return False
