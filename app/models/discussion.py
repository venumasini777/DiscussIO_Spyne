from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Discussion(Base):
    __tablename__ = 'discussions'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    image_url = Column(String, nullable=True)
    created_on = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    hashtags = Column(String)

    user = relationship("User", back_populates="discussions")
