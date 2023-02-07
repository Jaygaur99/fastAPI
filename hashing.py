from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def encrypt(password: str):
    return pwd_context.hash(password)


def verify(saved_password, hashed_password):
    return pwd_context.verify(hashed_password, saved_password)
