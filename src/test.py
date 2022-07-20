from DataAccess.team_dao import TeamDao
from DataAccess.match_dao import MatchDao
from DataAccess.models import Team, Match
from DataAccess import db


def run():
    pass


if __name__ == '__main__':
    db.base.metadata.create_all(db.connection)
    run()
