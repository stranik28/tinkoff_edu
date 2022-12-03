from app.adapters.match import MatchRepository
from app.database.connections import get_database_connection

def get_match_adapter():
    db = get_database_connection()
    return MatchRepository(next(db))