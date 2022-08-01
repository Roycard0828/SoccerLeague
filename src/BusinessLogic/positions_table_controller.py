from ..DataAccess.factory_dao import FactoryPositionsTableDao
from ..DataAccess.models import PositionsTable, Team
from .team_controller import TeamController


class PositionsTableController:

    @classmethod
    def register_all_teams(cls):
        dao = FactoryPositionsTableDao.create_entity()
        team_list = TeamController.get_all_teams()
        for team in team_list:
            table_team = PositionsTable(team)
            dao.save(table_team)

    @classmethod
    def update_team_points(cls, data_local_team: dict, data_visiting_team: dict):
        dao = FactoryPositionsTableDao.create_entity()
        local_team = dao.get_team_by_id(data_local_team['team_id'])[0]
        visiting_team = dao.get_team_by_id(data_visiting_team['team_id'])[0]

        def set_new_data(team: PositionsTable, data: dict):
            team.matches_played += 1
            team.matches_won += data['match_won']
            team.tied_matches += data['tie_match']
            team.matches_lost += data['match_lost']
            team.goals += data['goals']
            team.points += data['points']
            dao.update_team_data(team)

        set_new_data(local_team, data_local_team)
        set_new_data(visiting_team, data_visiting_team)

    @classmethod
    def read_all_teams(cls):
        dao = FactoryPositionsTableDao.create_entity()
        team_list = dao.get_all()
        return list(team_list)
