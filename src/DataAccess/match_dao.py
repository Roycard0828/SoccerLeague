from .models import Match
from .general_dao import GeneralDao
from .db import session


class MatchDao(GeneralDao):

    def __init__(self):
        self.session = session

    def save(self, match: Match):
        self.session.add(match)
        self.session.commit()
        return True

    def read_by_id(self, id: int):
        query = self.session.query(Match).get(id)
        return query

    def read_all(self):
        query = self.session.query(Match)
        return query

    def update(self, match: Match, *args):
        match = match
        match.day_number = args[0]
        match.local_team = args[1]
        match.visiting_team = args[2]
        match.field = args[3]
        match.result = args[4]

        self.session.add(match)
        self.session.commit()
        return True

    def delete(self, match: Match):
        self.session.delete(match)
        self.session.commit()
        return True
