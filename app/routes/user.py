from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.database import SessionLocal
from app.services.user_service import (
    create_user,
    update_user,
    delete_user,
    get_user_list,
    search_user_by_name,
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.put("/users/{user_id}", response_model=UserResponse)
def update_existing_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db=db, user_id=user_id, user=user)

@router.delete("/users/{user_id}")
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    delete_user(db=db, user_id=user_id)
    return {"message": "User deleted successfully"}

@router.get("/users/", response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = get_user_list(db=db, skip=skip, limit=limit)
    return users

@router.get("/users/search/", response_model=list[UserResponse])
def search_users(name: str, db: Session = Depends(get_db)):
    users = search_user_by_name(db=db, name=name)
    return users
