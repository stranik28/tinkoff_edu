from fastapi import APIRouter, Depends
from app.services.tournament import get_tournament_adapter
from app.schemas.tournament import Tournament, TournamentInDB

router = APIRouter(prefix="/tournament", tags=["tournament"])

@router.post("/")
async def create_tournament(tournament: Tournament, tournament_adapter=Depends(get_tournament_adapter)):
    return tournament_adapter.create(tournament)

@router.get("/{id}")
async def get_tournament(id: int, tournament_adapter=Depends(get_tournament_adapter)):
    return tournament_adapter.get_by_id(id)