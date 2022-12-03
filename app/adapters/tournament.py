from app.models.tournament import Tournament
from app.adapters.base import BaseAdapter
from app.schemas.tournament import Tournament as TournamentSchema

class TournamentRepository(BaseAdapter):
    def create(self, tournament: TournamentSchema):
        tournament = Tournament(**tournament.dict())
        tournament.status = "Active"
        self.session.add(tournament)
        self.session.commit()
        for i in range(0, tournament.number_of_rounds):
            self.create_round(tournament.id, i + 1)
        return tournament.id

    def get_by_id(self, id: int):
        return self.session.query(Tournament).filter(Tournament.id == id).first()

