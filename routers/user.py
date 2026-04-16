from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database
from auth import hash_password, verify_password, create_token

router = APIRouter()

# 🔐 Signup
@router.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(database.get_db)):

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


# 🔓 Login
@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(database.get_db)):

    db_user = db.query(models.User).filter(models.User.username == user.username).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    token = create_token({"sub": db_user.username})

    return {"access_token": token}