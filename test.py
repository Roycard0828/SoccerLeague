from src.DataAccess import db
from src.BusinessLogic.match_calendar import create_calendar
from src.BusinessLogic.match_controller import MatchController
from src.BusinessLogic.team_controller import TeamController


def run():
    create_calendar()


if __name__ == '__main__':
    db.base.metadata.create_all(db.connection)
    run()
