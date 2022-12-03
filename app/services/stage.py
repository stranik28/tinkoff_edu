from app.adapters.stage import StageAdapter
from app.database.connections import get_database_connection

def get_stage_adapter():
    db = get_database_connection()
    return StageAdapter(next(db))