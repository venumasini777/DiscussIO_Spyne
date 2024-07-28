from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    name: str
    mobile_no: str
    email: EmailStr
    pwd: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    mobile_no: Optional[str] = None
    email: EmailStr 

class UserResponse(BaseModel):
    id: int
    name: str
    mobile_no: str
    email: EmailStr

    class Config:
        orm_mode = True
