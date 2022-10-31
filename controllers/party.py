from controllers.abstract import CRUDController
from models.party import Party, PartyDoesNotExist
from repositories.party import PartyRepository


class PartyController(CRUDController):

    def __init__(self):
        self.repository = PartyRepository(
            model=Party,
            does_not_exist=PartyDoesNotExist
        )

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id_party):
        return self.repository.get_by_id(id_party)

    def create(self, content):
        created = Party(
            name=content["name"],
            slogan=content["slogan"],
        )
        return self.repository.save(created)

    def update(self, id_party, content):
        party = self.get_by_id(id_party)
        party.name = content["name"]
        party.slogan = content["slogan"]
        return self.repository.save(party)

    def delete(self, id_party):
        party = self.get_by_id(id_party)
        return self.repository.delete(party)

    def count(self):
        return self.repository.count()

