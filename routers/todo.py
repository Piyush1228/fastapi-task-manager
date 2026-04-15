from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, database

router = APIRouter()

@router.post("/todos")
def create(todo: schemas.Todo, db: Session = Depends(database.get_db)):
    return crud.create_todo(db, todo)

@router.get("/todos")
def read(db: Session = Depends(database.get_db)):
    return crud.get_todos(db)