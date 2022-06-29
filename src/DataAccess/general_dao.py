"""Abstract class to be implmented by its subclasess."""

from abc import ABC, abstractmethod


class GeneralDao(ABC):

    @abstractmethod
    def save(self, obj):
        pass

    @abstractmethod
    def read_by_id(self, id: int):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def update(self, obj, *args):
        pass

    @abstractmethod
    def delete(self, obj):
        pass
    