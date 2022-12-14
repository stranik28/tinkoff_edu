from app.models.stage import Stage
from app.adapters.base import BaseAdapter
import math

class StageAdapter(BaseAdapter):
    def create(self, number: int, tournament_id: int):
        ids = []
        for i in range(int(math.log(number,2))):
            stage = Stage(tournament_id=tournament_id, level=i)
            self.session.add(stage)
            self.session.commit()
            ids.append(stage.id)
        return ids