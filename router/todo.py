from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.todo import Todo as todo_schema
from database import get_database_session
from models.todo import Todo as todo_model

router = APIRouter(prefix="/todo")


@router.post("/")
def create(request: todo_schema, db: Session = Depends(get_database_session)):
    todo_item = todo_model(
        name=request.name, description=request.description, completed=request.completed)
    db.add(todo_item)
    db.commit()
    db.refresh(todo_item)
    return todo_item


@router.get("/{id}")
def read_todo(id: int):
    return "read todo item with id {id}"


@router.put("/{id}")
def update_todo(id: int):
    return "update todo item with id {id}"


@router.delete("/{id}")
def delete_todo(id: int):
    return "delete todo item with id {id}"


@router.get("/")
def read_todo_list():
    return "read todo list"
