from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from schemas.todo import Todo as todo_schema
from schemas.user import User as UserSchema
from database import get_database_session
from models.todo import Todo as todo_model
from models.user import User as UserModel
import oauth2

router = APIRouter(prefix="/todo", tags=["Todo"])

# POST Routes


@router.post("/")
def create(request: todo_schema, db: Session = Depends(get_database_session), current_user: UserSchema = Depends(oauth2.get_current_user)):
    user = db.query(UserModel).filter(
        UserModel.email == current_user.email).first()
    todo_item = todo_model(
        name=request.name, description=request.description, completed=request.completed, user_id=user.id)
    db.add(todo_item)
    db.commit()
    db.refresh(todo_item)
    return todo_item

# GET Routes


@router.get("/")
def read_todo_list(db: Session = Depends(get_database_session), current_user: UserSchema = Depends(oauth2.get_current_user)):
    user = db.query(UserModel).filter(
        UserModel.email == current_user.email).first()
    todo_list = db.query(todo_model).filter(
        todo_model.user_id == user.id).all()
    # print(todo_list)
    return todo_list


@router.get("/{id}")
def read_todo(id: int, db: Session = Depends(get_database_session), current_user: UserSchema = Depends(oauth2.get_current_user)):
    user = db.query(UserModel).filter(
        UserModel.email == current_user.email).first()
    todo_item = db.query(todo_model).filter(
        todo_model.id == id, todo_model.user_id == user.id)
    if not todo_item.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo item with id {id} not found"
        )
    return todo_item.first()


@router.put("/{id}")
def update_todo(id: int, request: todo_schema, db: Session = Depends(get_database_session), current_user: UserSchema = Depends(oauth2.get_current_user)):
    user = db.query(UserModel).filter(
        UserModel.email == current_user.email).first()
    item = db.query(todo_model).filter(
        todo_model.id == id, todo_model.user_id == user.id)
    if not item.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo Item with id {id} not found"
        )
    item.update(dict(request), synchronize_session=False)
    db.commit()
    return item.first()


@router.delete("/{id}")
def delete_todo(id: int, db: Session = Depends(get_database_session), current_user: UserSchema = Depends(oauth2.get_current_user)):
    user = db.query(UserModel).filter(
        UserModel.email == current_user.email).first()
    todo_item = db.query(todo_model).filter(
        todo_model.id == id, todo_model.user_id == user.id)
    if not todo_item.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo item with id {id} not found"
        )
    todo_item.delete(synchronize_session=False)
    db.commit()
    return {"message": "Removed"}
