from pydantic import BaseModel


class Team(BaseModel):
    name: str


class TeamInDB(Team):
    id: int
