from abc import ABC
from app.database.session import Session

class BaseAdapter(ABC):
    def __init__(self, session: Session):
        self.session: Session = session