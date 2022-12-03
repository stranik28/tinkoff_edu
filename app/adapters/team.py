from app.models.team import Team
from app.adapters.base import BaseAdapter
from app.schemas.team import Team as TeamSchema


class TeamAdapter(BaseAdapter):
    def create(self, team: TeamSchema):
        team = Team(**team.dict())
        self.session.add(team)
        self.session.commit()
        return team.id

    def get_by_id(self, id: int):
        return self.session.query(Team).filter(Team.id == id).first()
    
    def get_all(self):
        return self.session.query(Team).all()

