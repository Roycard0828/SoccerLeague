from abc import ABC, abstractmethod
from .team_dao import TeamDao
from .match_dao import MatchDao
from .positions_table_dao import PositionsTableDao


class EntityFactory(ABC):

    @abstractmethod
    def create_entity(self):
        pass


class FactoryTeamDao(EntityFactory):

    @classmethod
    def create_entity(cls):
        return TeamDao()


class FactoryMatchDao(EntityFactory):

    @classmethod
    def create_entity(cls):
        return MatchDao()


class FactoryPositionsTableDao(EntityFactory):

    @classmethod
    def create_entity(cls):
        return PositionsTableDao()
