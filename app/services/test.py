from app.adapters.test import TestAdapter
from app.database.connections import get_database_connection

def get_test_adapter():
    db = get_database_connection()
    return TestAdapter(next(db))