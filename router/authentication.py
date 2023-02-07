from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_database_session
from schemas.auth import AuthSchema
from models.user import User as UserModel
import jwt_token
from hashing import verify as verify_hash

router = APIRouter(tags=["Authentication"])


@router.post('/login')
def login(request: AuthSchema, db: Session = Depends(get_database_session)):
    user = db.query(UserModel).filter(UserModel.email == request.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    if not verify_hash(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Credentials"
        )

    access_token = jwt_token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
