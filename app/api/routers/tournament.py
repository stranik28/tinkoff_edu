from fastapi import APIRouter, Depends
from app.services.tournament import get_tournament_adapter
from app.schemas.tournament import Tournament, TournamentInDB
from app.services.stage import get_stage_adapter
from app.services.match import get_match_adapter
from app.schemas.team import Team
from app.services.team import get_team_adapter

router = APIRouter(prefix="/api/tournaments", tags=["tournament"])


@router.post("/")
async def create_tournament(tournament: Tournament, tournament_adapter=Depends(get_tournament_adapter),\
    stage_adapter=Depends(get_stage_adapter), match_adapter=Depends(get_match_adapter)):
    id = tournament_adapter.create(tournament)
    ids = stage_adapter.create(4, id)
    print(ids)
    match_adapter.create(len(ids), ids)
    return {"id": id}

@router.get("/teams")
async def get_teams(team_adapter=Depends(get_team_adapter)):
    return team_adapter.get_all()

@router.get("/{id}")
async def get_tournament(id: int, tournament_adapter=Depends(get_tournament_adapter)):
    return tournament_adapter.get_by_id(id)


@router.put("/{id}/matches/{match_id}")
async def set_score(id: int, match_id: int, match_adapter=Depends(get_match_adapter), score1:int=None, score2:int=None):
    match_adapter.set_score(id, match_id, score1,score2)
    return {"is_finished": False}

@router.post("/teams")
async def add_team(team: Team, team_adapter=Depends(get_team_adapter)):
    return team_adapter.create(team)

