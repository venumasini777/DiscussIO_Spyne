import logging
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import User
from app.schemas.user import UserCreate, UserUpdate
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


logger = logging.getLogger(__name__)

def get_sha256_hash(password: str) -> str:
    # Create a SHA-256 hash object
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    # Update the hash object with the salt and password bytes
    digest.update(password.encode('utf-8'))
    # Finalize the hash and return the hexadecimal representation
    return digest.finalize().hex()

hashed_password = get_sha256_hash("Venu71198")
logger.info(hashed_password)



def create_user(db: Session, user: UserCreate):
    db_user = db.query(User).filter_by(email == user.email).first()
    if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_sha256_hash(user.password)
    db_user = User(
        name=user.name,
        mobile_no=user.mobile_no,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()

def get_user_list(db: Session, skip: int, limit: int):
    return db.query(User).offset(skip).limit(limit).all()

def search_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name.ilike(f"%{name}%")).all()
