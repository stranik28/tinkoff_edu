from sqlalchemy import Column, Integer, String, ARRAY
from app.database.base import Base


class Tournament(Base):
    __tablename__ = "tournament_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)
    stages = Column(ARRAY(Integer))

