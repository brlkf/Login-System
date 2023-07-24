import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware to allow requests from all origins during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple User model for login data
class User(BaseModel):
    username: str
    password: str

# Function to verify if a user exists and their credentials are valid
def verify_user(user: User):
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT username, password FROM users WHERE username = ?", (user.username,))
        user_data = cursor.fetchone()

        if user_data is None or user_data[1] != user.password:
            raise HTTPException(status_code=401, detail="Incorrect username or password")

        return {"message": "Login successful"}

# Route for user login
@app.post('/login')
def login(user: User):
    return verify_user(user)
