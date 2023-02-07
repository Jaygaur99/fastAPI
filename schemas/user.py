from pydantic import BaseModel
from schemas.todo import ShowTodo


class User(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class ShowUser(User):

    class Config:
        orm_mode = True


class ShowUserTodo(ShowUser):
    todos: list[ShowTodo] = []

    class Config:
        orm_mode = True
