import os
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

# Set up database connection and session
DATABASE_URI = "mssql+pyodbc://sa:123Tralala^@localhost/Escaperoom?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Define the Pydantic model for the user registration request
class UserRegistration(BaseModel):
    username: str
    password: str


app = FastAPI()


@app.post("/register")
def register_user(registration_data: UserRegistration, db: SessionLocal):
    username = registration_data.username
    password = registration_data.password

    # Check if the username is already taken
    existing_user = db.query(UserRegistration).filter(UserRegistration.username == username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    # Create a new user object and add it to the database
    new_user = UserRegistration(username=username, password=password)
    db.add(new_user)
    db.commit()

    return {"message": "Successfully registered new user"}
