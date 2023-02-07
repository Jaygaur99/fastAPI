"""
    Following script is responsible for encrypting and matching the 
    password 
"""


from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def encrypt(password: str):
    """
        Function to get encrypted password
        For more info check docs here https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
    """
    return pwd_context.hash(password)


def verify(saved_password, hashed_password):
    """
        Function to match passwords
        For more info check docs here https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
    """
    return pwd_context.verify(hashed_password, saved_password)
