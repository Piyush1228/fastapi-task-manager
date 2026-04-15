from fastapi import FastAPI
from routers import todo, user
from database import engine, Base
import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(todo.router)
app.include_router(user.router)