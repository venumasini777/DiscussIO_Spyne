from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Discussion(Base):
    __tablename__ = 'discussions'

    id = Column(Integer, primary_key=True, index=True,autoincrement = True)
    content = Column(String)
    created_on = Column(DateTime, default=datetime.utcnow)
    updated_on = Column(DateTime, nullable = True)
    image = Column(String, nullable=True)
    hashtags = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="discussions")
