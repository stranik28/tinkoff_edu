from sqlalchemy.orm import sessionmaker
from app.database.base import engine
from sqlalchemy.orm import Session

SessionLocal: Session = sessionmaker(
    autocommit=False, autoflush=True, bind=engine)