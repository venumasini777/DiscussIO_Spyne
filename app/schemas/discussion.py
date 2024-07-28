from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime




class DiscussionCreate(BaseModel):
    content: str
    image: str
    hashtags: str
    user_id: int

class DiscussionUpdate(BaseModel):
    text: str
    image_url: str = None
    hashtags: str

class DiscussionResponse(BaseModel):
    id: int
    content: str
    created_on: datetime
    image: str
    #hashtags: str
    user_id: int

    class Config:
        orm_mode = True
