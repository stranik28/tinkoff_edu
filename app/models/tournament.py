from sqlalchemy import Column, Integer, String
from app.database.base import Base


class Tournament(Base):
    __tablename__ = "tournament_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    status = Column(String)

