from app.models.tournament import Tournament
from app.adapters.base import BaseAdapter
from app.schemas.tournament import Tournament as TournamentSchema
from app.models.stage import Stage
from app.models.match import Match

class TournamentRepository(BaseAdapter):
    def create(self, tournament: TournamentSchema):
        tournament = Tournament(**tournament.dict())
        tournament.status = "Active"
        self.session.add(tournament)
        self.session.commit()
        return tournament.id

    def get_by_id(self, id: int):
        tournament = self.session.query(Tournament).filter(Tournament.id == id).first()
        # Tournament model to dict
        tournament1 = tournament.__dict__
        # print(tournament1)
        stages = self.session.query(Stage).filter(Stage.tournament_id == id).all()
        tournament1['stages'] = []
        for i in stages:
            stage = i.__dict__
            matches = self.session.query(Match).filter(Match.stage_id == stage['id']).all()
            stage['matches'] = []
            for j in matches:
                match = j.__dict__
                stage['matches'].append(match)
            tournament1['stages'].append(stage)
        return tournament1

