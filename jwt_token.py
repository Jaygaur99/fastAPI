from datetime import timedelta, datetime
from jose import JWTError, jwt
from fastapi import HTTPException
import schemas.auth as auth

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


def create_access_token(data: dict):
    """
        Function to generate access token
        For more info check docs here https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=24)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception: HTTPException):
    """
        Function to verify JWT Token
        For more info check docs here https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        # print("TOKENDATA: ", auth.TokenData(email=email))
        return auth.TokenData(email=email)
    except JWTError:
        raise credentials_exception
