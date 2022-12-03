from app.models.match import Match
from app.adapters.base import BaseAdapter
from app.schemas.match import Match as MatchSchema
from app.models.stage import Stage
from app.models.team import Team

class MatchRepository(BaseAdapter):
    def create(self, number: int, stages_ids: list):
        # Get all teams ids
        teams_ids = [team.id for team in self.session.query(Team).all()]
        tem_id = 0
        for i in reversed(range(1,number+1)):
            for j in range(i**2):
                if i == number:
                    match = Match(stage_id=stages_ids[number-i], team1 = teams_ids[tem_id], team2 = teams_ids[tem_id+1], score1 = None, score2 = None)
                    tem_id += 2
                else:
                    match = Match(stage_id=stages_ids[number-i], team1 = None, team2 = None, score1 = None, score2 = None)
                self.session.add(match)
        self.session.commit()
        return match.id
            
            