"""
    Authentication Routes
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.database import get_database_session
from fastapi.security import OAuth2PasswordRequestForm
from core.models.user import User as UserModel
from services.jwt_token import create_access_token
from services.hashing import verify as verify_hash

router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_database_session)
):
    """
        Function to make the user log in and generate the jwt_token for the user
    """
    # Get the user
    user = db.query(UserModel).filter(
        UserModel.email == request.username).first()
    # User does not exist
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )
    # password check
    if not verify_hash(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Credentials"
        )

    # JWT
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
