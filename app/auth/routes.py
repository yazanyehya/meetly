from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.auth.models import User

router = APIRouter()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define the request model for signup
class SignupRequest(BaseModel):
    name: str
    email: EmailStr 
    password: str
    role: str = "user"  

@router.post("/signup")
def signup(data: SignupRequest, db: Session = Depends(get_db)):
    # Check if the email already exists
    user = db.query(User).filter(User.email == data.email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create a new user
    new_user = User(
        name=data.name,
        email=data.email,
        password=data.password,
        role=data.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user_id": new_user.id}
