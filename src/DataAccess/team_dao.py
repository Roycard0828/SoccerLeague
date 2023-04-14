from .models import Team
from .general_dao import GeneralDao
from .db import session


class TeamDao(GeneralDao):

    def __init__(self):
        self.session = session

    def save(self, team: Team):
        self.session.add(team)
        self.session.commit()
        return True

    def read_by_id(self, id: int):
        query = self.session.query(Team).get(id)
        return query

    def read_all(self):
        query = self.session.query(Team).order_by(Team.id.asc())
        return query

    def update(self, team: Team, *args):
        team = team
        team.name = args[0]
        team.manager = args[1]
        team.field = args[2]

        self.session.add(team)
        self.session.commit()
        return True

    def delete(self, team: Team):
        self.session.delete(team)
        self.session.commit()
        return True
