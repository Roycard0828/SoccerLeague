"""Abstract class to be implmented by its subclasess."""

from abc import ABC, abstractmethod


class GeneralDao(ABC):

    @abstractmethod
    def save(self, object):
        pass

    @abstractmethod
    def readById(self, id: int):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def updateById(self, id: int, *args):
        pass

    @abstractmethod
    def delete(self, object):
        pass
    