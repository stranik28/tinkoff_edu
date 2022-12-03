from app.models.match import Match
from app.adapters.base import BaseAdapter
from app.schemas.match import Match as MatchSchema
from app.models.stage import Stage

class MatchRepository(BaseAdapter):
    def create(self, number: int, stages_ids: list):
        for i in reversed(range(1,number+1)):
            for j in range(i**2):
                match = Match(stage_id=stages_ids[number-i], team1 = 1, team2 = 2, score1 = 0, score2 = 0)
                self.session.add(match)
        self.session.commit()
        return match.id
            
            