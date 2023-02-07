from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from schemas.todo import Todo as todo_schema
from database import get_database_session
from models.todo import Todo as todo_model

router = APIRouter(prefix="/todo", tags=["Todo"])

# POST Routes


@router.post("/")
def create(request: todo_schema, db: Session = Depends(get_database_session)):
    todo_item = todo_model(
        name=request.name, description=request.description, completed=request.completed)
    db.add(todo_item)
    db.commit()
    db.refresh(todo_item)
    return todo_item

# GET Routes


@router.get("/")
def read_todo_list(db: Session = Depends(get_database_session)):
    todo_list = db.query(todo_model).all()
    return todo_list


@router.get("/{id}")
def read_todo(id: int, db: Session = Depends(get_database_session)):
    todo_item = db.query(todo_model).filter(todo_model.id == id)
    if not todo_item.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo item with id {id} not found"
        )
    return todo_item.first()


@router.put("/{id}")
def update_todo(id: int, request: todo_schema, db: Session = Depends(get_database_session)):
    item = db.query(todo_model).filter(todo_model.id == id)
    if not item.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo Item with id {id} not found"
        )
    item.update(dict(request), synchronize_session=False)
    db.commit()
    return item.first()


@router.delete("/{id}")
def delete_todo(id: int, db: Session = Depends(get_database_session)):
    todo_item = db.query(todo_model).filter(todo_model.id == id)
    if not todo_item.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo item with id {id} not found"
        )
    todo_item.delete(synchronize_session=False)
    db.commit()
    return {"message": "Removed"}
