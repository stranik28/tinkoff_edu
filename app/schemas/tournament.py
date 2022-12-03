from pydantic import BaseModel


class Tournament(BaseModel):
    name: str
    status: str


class TournamentInDB(Tournament):
    id: int
