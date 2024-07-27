from sqlalchemy import Column, Integer, String, UniqueConstraint
from app.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    mobile_no = Column(String(15), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)

    __table_args__ = (UniqueConstraint('mobile_no', 'email', name='unique_user'),)
