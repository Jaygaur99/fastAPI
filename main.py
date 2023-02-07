import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from v1.router.todo import router as todo_router
from v1.router.user import router as user_router
from v1.router.authentication import router as auth_router
from core.models import todo, user
from services.database import engine

app = FastAPI()

# Check and Update Models
todo.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)

# Routers
app.include_router(todo_router)
app.include_router(user_router)
app.include_router(auth_router)


@app.route("/")
def home(request):
    return RedirectResponse("/docs")

# if __name__ == '__main__':
#     uvicorn.run(port=8000, host="127.0.0.1", app=app)
