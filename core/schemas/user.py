from pydantic import BaseModel
from core.schemas.todo import ShowTodo


class User(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class ShowUserTodo(BaseModel):
    name: str
    email: str
    todos: list[ShowTodo] = []

    class Config:
        orm_mode = True
