from sqlalchemy import Column, Integer, ForeignKey
from app.database.base import Base


class Match(Base):
    __tablename__ = "match_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    score1 = Column(Integer)
    score2 = Column(Integer)
    team1 = Column(Integer, ForeignKey("team_table.id"))
    team2 = Column(Integer, ForeignKey("team_table.id"))
    stage_id = Column(Integer, ForeignKey("stage_table.level"))
