from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    mobile_no = Column(String(15), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    pwd = Column(String(256))

    discussions = relationship('Discussion', back_populates='user')

    __table_args__ = (UniqueConstraint('mobile_no', 'email', name='unique_user'),)
