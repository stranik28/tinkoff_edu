from pydantic import BaseModel


class Stage(BaseModel):
    matches: int
    level: int
    tournament_id: id


class StageInDB(Stage):
    id: int
