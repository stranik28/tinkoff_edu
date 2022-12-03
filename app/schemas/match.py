from pydantic import BaseModel


class Match(BaseModel):
    name: str
    team1: int
    team1: int
    score1: int
    score2: int
    stage_id: int


class MatchInDB(Match):
    id: int
