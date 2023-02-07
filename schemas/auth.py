from pydantic import BaseModel


class AuthSchema(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True
