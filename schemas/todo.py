from pydantic import BaseModel


class Todo(BaseModel):
    name: str
    description: str
    completed: bool | None = False

    class Config:
        orm_mode = True


class ShowTodo(Todo):
    id: int

    class Config:
        orm_mode = True
