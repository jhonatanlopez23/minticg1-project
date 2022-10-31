from abc import ABC, abstractmethod


class CRUDController(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id_item):
        pass

    @abstractmethod
    def create(self, content):
        pass

    @abstractmethod
    def update(self, id_item, content):
        pass

    @abstractmethod
    def delete(self, id_item):
        pass

    @abstractmethod
    def count(self):
        pass
