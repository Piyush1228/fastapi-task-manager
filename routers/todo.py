from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database
from auth import get_current_user

router = APIRouter()


# ➕ Create Todo
@router.post("/todos")
def create_todo(
    todo: schemas.Todo,
    db: Session = Depends(database.get_db),
    current_user: str = Depends(get_current_user)
):

    user = db.query(models.User).filter(models.User.username == current_user).first()

    new_todo = models.Todo(
        id=todo.id,
        title=todo.title,
        completed=todo.completed,
        user_id=user.id
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


# 📋 Get Todos (ONLY current user)
@router.get("/todos")
def get_todos(
    db: Session = Depends(database.get_db),
    current_user: str = Depends(get_current_user)
):

    user = db.query(models.User).filter(models.User.username == current_user).first()

    todos = db.query(models.Todo).filter(models.Todo.user_id == user.id).all()

    return todos