from pydantic import BaseModel


class Tournament(BaseModel):
    name: str


class TournamentInDB(Tournament):
    id: int
    status: str
