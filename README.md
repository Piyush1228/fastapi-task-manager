# 🚀 FastAPI Task Manager API

A secure backend API built using FastAPI, PostgreSQL, and JWT Authentication.

---

## 🔥 Features

* User Signup & Login (JWT Authentication)
* Password hashing using bcrypt
* Protected routes (only authenticated users can access)
* CRUD operations for Todos
* User-specific tasks (each user sees only their own todos)
* PostgreSQL database integration

---

## 🛠 Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT (python-jose)
* Passlib (bcrypt)

---

## 📌 API Endpoints

### 👤 Authentication

* `POST /signup` → Create new user
* `POST /login` → Get JWT token

### 📋 Todos

* `POST /todos` → Create todo (Protected)
* `GET /todos` → Get all todos (Protected)
* `PUT /todos/{id}` → Update todo
* `DELETE /todos/{id}` → Delete todo

---

## 🔐 Authentication Flow

1. Signup → Create account
2. Login → Get JWT token
3. Use token in Authorization header:

```
Bearer YOUR_TOKEN
```

4. Access protected routes

---

## ⚙️ Setup Instructions

1. Clone the repository
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Setup PostgreSQL database
4. Run the server:

```
uvicorn main:app --reload
```

---

## 💡 Future Improvements

* Role-based authentication
* Refresh tokens
* Deployment (Render/Railway)
* Frontend integration

---

## 👨‍💻 Author

Piyush Kumar