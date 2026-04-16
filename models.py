from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base

# 👤 User Table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)


# 📋 Todo Table
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("users.id"))