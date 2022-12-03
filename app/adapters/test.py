from app.adapters.base import BaseAdapter
from app.models.team import Team
# from app.database.base import

class TestAdapter(BaseAdapter):
    def get_all(self):
        return self.session.query(Team).all()

