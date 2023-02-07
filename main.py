from fastapi import FastAPI
from router.todo import router as todo_router
from models import todo
from database import engine

app = FastAPI()

todo.Base.metadata.create_all(bind=engine)

app.include_router(todo_router)


@app.get("/")
def root():
    return {"Message": "HELLO World"}
