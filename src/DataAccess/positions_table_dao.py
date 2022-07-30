from.models import PositionsTable
from.db import session


class PositionsTableDao:

    def __init__(self):
        self.session = session

    def save(self, table_team: PositionsTable):
        self.session.add(table_team)
        self.session.commit()
        return True

    def get_all(self):
        query = self.session.query(PositionsTable).order_by(PositionsTable.puntos.desc())
        return query

    def get_team_by_id(self, team_id: int):
        query = self.session.query(PositionsTable).filter(
            PositionsTable.team_id == team_id
        )
        return query

    def update_team_data(self, table_team: PositionsTable):
        self.session.add(table_team)
        self.session.commit()
        return True
