from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_database_session
from schemas.user import User as UserSchema
from models.user import User as UserModel
from hashing import encrypt

router = APIRouter(tags=["User"], prefix="/user")


@router.post("/")
def create_user(request: UserSchema, db: Session = Depends(get_database_session)):
    try:
        hashed_password = encrypt(request.password)
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


@router.get("/{id}")
def get_user(id: int, db: Session = Depends(get_database_session)):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    return user
