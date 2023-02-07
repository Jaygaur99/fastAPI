from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_database_session
from schemas.user import User as UserSchema, ShowUserTodo as ShowUserTodoSchema, ShowUser as ShowUserSchema
from models.user import User as UserModel
from hashing import encrypt
from utils import validate_email

router = APIRouter(tags=["User"], prefix="/user")


@router.post("/", response_model=ShowUserTodoSchema)
def create_user(request: UserSchema, db: Session = Depends(get_database_session)):
    if not validate_email(request.email):
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is not valid"
        )
    hashed_password = encrypt(request.password)
    try:
        new_user = UserModel(
            name=request.name, email=request.email, password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occured or user already exists"
        )


# @router.get("/{id}", response_model=ShowUserSchema)
# def get_user(id: int, db: Session = Depends(get_database_session)):
#     user = db.query(UserModel).filter(UserModel.id == id).first()
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
#         )
#     return user
