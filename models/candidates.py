from bson import DBRef, ObjectId

from models.abstract import AbstractModel, ElementDoesNotExist
from models.party import Party


class Candidate(AbstractModel):
    COLLECTION_NAME = "candidates"

    resolution_number = None
    names = None
    last_names = None
    identification = None
    party: Party = None

    def __init__(self, resolution_number, names, last_names, identification, party=None, _id=None):
        super().__init__(_id)
        self.resolution_number = resolution_number
        self.names = names
        self.last_names = last_names
        self.identification = identification
        self.party = party

    def prepare_to_save(self):
        party_db_ref = None
        if self.party:
            party_db_ref = DBRef(
                id=ObjectId(self.party._id),
                collection=Party.COLLECTION_NAME
            )
        return {
            "resolution_number": self.resolution_number,
            "names": self.names,
            "last_names": self.last_names,
            "identification": self.identification,
            "party": party_db_ref
        }

    def to_json(self):
        party = None
        if self.party:
            party = self.party.to_json()
        return {
            "_id": self._id,
            "resolution_number": self.resolution_number,
            "names": self.names,
            "last_names": self.last_names,
            "identification": self.identification,
            "party": party
        }

    @staticmethod
    def create(doc):
        party = None
        if doc.get("party"):
            party = Party.create(doc.get("party"))
        return Candidate(
            resolution_number=doc["resolution_number"],
            names=doc["names"],
            last_names=doc["last_names"],
            identification=doc["identification"],
            party=party,
            _id=str(doc["_id"]) if doc.get("_id") else None,
        )


class CandidateDoesNotExist(ElementDoesNotExist):
    pass
