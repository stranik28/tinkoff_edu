from app.adapters.team import TeamAdapter
from app.database.connections import get_database_connection


def get_team_adapter():
    db = get_database_connection()
    return TeamAdapter(next(db))
