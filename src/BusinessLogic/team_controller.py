""" Class to make a connection with the DataAccess package """

from ..DataAccess.factory_dao import FactoryTeamDao
from ..DataAccess.models import Team


class TeamController:

    dao = FactoryTeamDao.create_entity()

    @classmethod
    def add_team(cls, name: str, manager: str, field: str):
        team = Team(name, manager, field)
        cls.dao.save(team)

    @classmethod
    def delete_team(cls, id):
        team = cls.dao.read_by_id(id)
        if team is not None:
            cls.dao.delete(team)
            return True
        else:
            return False

    @classmethod
    def update_team(cls, id, name: str, manager: str, field: str):
        team = cls.dao.read_by_id(id)
        name = name
        manager = manager
        field = field
        if team is not None:
            cls.dao.update(team, name, manager, field)
            return True
        else:
            return False

    @classmethod
    def get_all_teams(cls):
        team_list = list(cls.dao.read_all())
        return team_list

    @classmethod
    def get_team_by_id(cls, id):
        team = cls.dao.read_by_id(id)
        return team
