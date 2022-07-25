from DataAccess.team_dao import TeamDao
from BusinessLogic.match_controller import MatchController
from DataAccess.models import Team, Match
from DataAccess import db


def run():
    team1 = MatchController.get_match_by_id(1)
    team2 = MatchController.get_match_by_id(1)

    MatchController.add_match(1, team1, team2, team1.field)


if __name__ == '__main__':
    db.base.metadata.create_all(db.connection)
    run()
