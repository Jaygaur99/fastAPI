import uvicorn
from fastapi import FastAPI
from router.todo import router as todo_router
from router.user import router as user_router
from router.authentication import router as auth_router
from models import todo, user
from database import engine

app = FastAPI()

# Check and Update Models
todo.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)

# Routers
app.include_router(todo_router)
app.include_router(user_router)
app.include_router(auth_router)


# if __name__ == '__main__':
#     uvicorn.run(port=8000, host="127.0.0.1", app=app)
