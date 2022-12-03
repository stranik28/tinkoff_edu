from app.models.match import Match
from app.adapters.base import BaseAdapter
from app.schemas.match import Match as MatchSchema
from app.models.stage import Stage
from app.models.team import Team
from app.models.tournament import Tournament

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

    def set_score(self, id: int, match_id: int, score1: int, score2: int):
        match = self.session.query(Match).filter(Match.id == match_id).first()
        match.score1 = score1
        match.score2 = score2
        self.session.commit()
        # If match is final, set tournament status to FINISHED
        if match.stage_id == id:
            tournament = self.session.query(Tournament).filter(Tournament.id == id).first()
            tournament.status = "FINISHED"
            self.session.commit()
            return {"is_finished": True}
        # Winner of match go to next stage
        # Get next stage id
        stage = self.session.query(Stage).filter(Stage.id == match.stage_id).first()
        next_stage_id = stage.id + 1
        # Get all matches of next stage
        matches = self.session.query(Match).filter(Match.stage_id == next_stage_id).all()
        # move winner to next stage in matche where team1 or team2 is None
        for i in matches:
            if i.team1 == None:
                i.team1 = match.team1
                break
            elif i.team2 == None:
                i.team2 = match.team1
                break
        self.session.commit()
        return {"is_finished": False}
            
            