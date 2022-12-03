from sqlalchemy import Column, Integer
from app.database.base import Base


class Match(Base):
    __tablename__ = "match_table"

    id = Column(Integer, primary_key=True)
    score1 = Column(Integer)
    score2 = Column(Integer)

