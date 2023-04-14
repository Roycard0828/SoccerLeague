from src.DataAccess import db
from src.BusinessLogic.match_calendar import create_calendar
from src.BusinessLogic.match_controller import MatchController
from src.BusinessLogic.team_controller import TeamController
from src.BusinessLogic.positions_table_controller import PositionsTableController
from src.BusinessLogic.positions_table_logic import start_season, end_soccer_day


def run():
    pass


if __name__ == '__main__':
    db.base.metadata.create_all(db.connection)
    run()
