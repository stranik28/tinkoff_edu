from sqlalchemy import Column, Integer, String
from app.database.base import Base


class Team(Base):
    __tablename__ = "team_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
