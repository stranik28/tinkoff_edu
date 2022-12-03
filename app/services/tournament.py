from app.repositories.tournament import TournamentRepository
from app.database.connections import get_database_connection

def get_tournament_repository():
    db = get_database_connection()
    return TournamentRepository(next(db))