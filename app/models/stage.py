from sqlalchemy import Column, Integer, String, ARRAY
from app.database.base import Base


class Stage(Base):
    __tablename__ = "stage_table"

    level = Column(Integer, primary_key=True)
    Matches = Column(ARRAY(Integer))

