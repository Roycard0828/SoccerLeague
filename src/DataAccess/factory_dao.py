from abc import ABC, abstractmethod
from .team_dao import TeamDao


class EntityFactory(ABC):

    @abstractmethod
    def create_entity(self):
        pass


class FactoryTeamDao(EntityFactory):

    @classmethod
    def create_entity(cls):
        return TeamDao()
