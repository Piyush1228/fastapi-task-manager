import models
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_todo(db: Session, todo):
    existing = db.query(models.Todo).filter(models.Todo.id == todo.id).first()

    if existing:
        raise HTTPException(status_code=400, detail="ID already exists")
    
    new_todo = models.Todo(
        id=todo.id,
        title=todo.title,
        completed=todo.completed
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def get_todos(db: Session):
    return db.query(models.Todo).all()