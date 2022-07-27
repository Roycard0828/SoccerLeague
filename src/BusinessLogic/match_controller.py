from ..DataAccess.factory_dao import FactoryMatchDao
from ..DataAccess.models import Match, Team


class MatchController:

    dao = FactoryMatchDao.create_entity()

    @classmethod
    def add_match(cls, day_number: int, local_team: Team, visiting_team: Team, field: str):
        match = Match(day_number, local_team, visiting_team, field)
        cls.dao.save(match)
        return True

    @classmethod
    def get_all_matches(cls):
        match_list = list(cls.dao.read_all())
        return match_list

    @classmethod
    def get_match_by_id(cls, id: int):
        match = cls.dao.read_by_id(id)
        return match

    @classmethod
    def get_all_matches_by_day_number(cls, day_number: int):
        match_list = list(cls.dao.read_by_day_number(day_number))
        return match_list

    @classmethod
    def update_result(cls, id: int, result: str):
        cls.dao.update_result(id, result)
