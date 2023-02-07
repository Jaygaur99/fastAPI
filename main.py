from fastapi import FastAPI
from router.todo import router as todo_router
from router.user import router as user_router
from models import todo, user
from database import engine

app = FastAPI()

todo.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)

app.include_router(todo_router)
app.include_router(user_router)
