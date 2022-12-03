from app.models.tournament import Tournament
from app.repositories.base import BaseRepository

class TournamentRepository(BaseRepository):
    def create(self, tournament):
        