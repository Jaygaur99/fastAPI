from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from services import jwt_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(data: str = Depends(oauth2_scheme)):
    """
        Function to get current user by matching JWT Token
        For more info check docs here https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # print(data)
    return jwt_token.verify_token(data, credentials_exception)
