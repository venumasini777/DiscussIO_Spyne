from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    mobile_no: str
    email: EmailStr

class UserUpdate(BaseModel):
    name: str
    mobile_no: str
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    mobile_no: str
    email: EmailStr

    class Config:
        orm_mode = True
