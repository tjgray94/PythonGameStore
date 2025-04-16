from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from model.User import User
from schemas.UserSchema import UserCreate, UserResponse
from passlib.context import CryptContext

router = APIRouter(prefix="/api/users", tags=["users"])

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Helper function to hash password
def hash_password(password: str):
  return pwd_context.hash(password)


# Get all users
@router.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
  return db.query(User).all()


# Get user by ID
@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.userid == user_id).first()
  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  return user


# Create a new user
@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
  # Check if email already exists
  existing_user = db.query(User).filter(User.email == user.email).first()
  if existing_user:
    raise HTTPException(status_code=400, detail="Email already in use")

  # Hash the password
  hashed_password = hash_password(user.password)

  # Create the new user
  new_user = User(name=user.name, email=user.email, password=hashed_password)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)

  return new_user


# Update user
@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserCreate, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.userid == user_id).first()
  if not user:
    raise HTTPException(status_code=404, detail="User not found")

  # Update user fields
  user.name = user_update.name
  user.email = user_update.email
  user.password = hash_password(user_update.password)  # Update password as well
  db.commit()
  db.refresh(user)

  return user


# Delete user by ID
@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.userid == user_id).first()
  if not user:
    raise HTTPException(status_code=404, detail="User not found")

  db.delete(user)
  db.commit()
  return


# Delete all users
@router.delete("/", status_code=204)
def delete_all_users(db: Session = Depends(get_db)):
  db.query(User).delete()
  db.commit()
  return
