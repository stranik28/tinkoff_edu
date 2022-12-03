from sqlalchemy import Column, Integer, ForeignKey
from app.database.base import Base


class Stage(Base):
    __tablename__ = "stage_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    level = Column(Integer)
    tournament_id = Column(Integer, ForeignKey('tournament_table.id'))

