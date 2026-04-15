from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database
from auth import hash_password

router = APIRouter()

@router.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(database.get_db)):

    # duplicate check
    existing = db.query(models.User).filter(models.User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed = hash_password(user.password)

    new_user = models.User(
        username=user.username,
        password=hashed
    )

    db.add(new_user)
    db.commit()

    return {"message": "User created"}

from auth import verify_password, create_token

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(database.get_db)):

    db_user = db.query(models.User).filter(models.User.username == user.username).first()

    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_token({"sub": db_user.username})

    return {"access_token": token}