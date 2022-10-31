from bson import DBRef, ObjectId

from models.abstract import AbstractModel, ElementDoesNotExist
from models.candidates import Candidate
from models.tables import Tables


class Results(AbstractModel):
    COLLECTION_NAME = "results"

    number_votes: int = None
    candidate: Candidate = None
    table: Tables = None

    def __init__(self,
                 number_votes,
                 candidate,
                 table,
                 _id=None):
        super().__init__(_id)
        self.number_votes = number_votes
        self.candidate = candidate
        self.table = table

    def prepare_to_save(self):
        print("")
        return {
            "number_votes": self.number_votes,
            "candidate": DBRef(
                id=ObjectId(self.candidate._id),
                collection=Candidate.COLLECTION_NAME
            ),
            "table": DBRef(
                id=ObjectId(self.table._id),
                collection=Tables.COLLECTION_NAME
            )
        }

    def to_json(self):
        return {
            "_id": self._id,
            "number_votes": self.number_votes,
            "candidate": self.candidate.to_json(),
            "table": self.table.to_json()
        }

    @staticmethod
    def create(doc):
        assert doc.get("candidate")
        assert doc.get("table")
        candidate = Candidate.create(doc.get("candidate"))
        table = Tables.create(doc.get("table"))
        return Results(
            number_votes=doc.get("number_votes"),
            candidate=candidate,
            table=table
        )


class ResultsDoesNotExist(ElementDoesNotExist):
    pass
