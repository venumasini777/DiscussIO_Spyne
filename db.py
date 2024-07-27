from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://admin:Spyne_123@discussio.cb8kmq6im8lj.ap-south-1.rds.amazonaws.com:3306/discussio"

engine = create_engine(DATABASE_URL)
print(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
