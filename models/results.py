from bson import DBRef, ObjectId

from models.abstract import AbstractModel, ElementDoesNotExist
from models.candidates import Candidate
from models.tables import Tables


class Results(AbstractModel):
    COLLECTION_NAME = "results"

    number_votes: int = None
    table: Tables = None
    candidate: Candidate = None

    def __init__(self,
                 number_votes,
                 candidate,
                 table,
                 _id=None):
        super().__init__(_id)
        self.number_votes = number_votes
        self.table = table
        self.candidate = candidate

    def prepare_to_save(self):
        print("")
        return {
            "number_votes": self.number_votes,
            "table": DBRef(
                id=ObjectId(self.table._id),
                collection=Tables.COLLECTION_NAME
            ),
            "candidate": DBRef(
                id=ObjectId(self.candidate._id),
                collection=Candidate.COLLECTION_NAME
            ),

        }

    def to_json(self):
        return {
            "_id": self._id,
            "number_votes": self.number_votes,
            "table": self.table.to_json(),
            "candidate": self.candidate.to_json(),

        }

    @staticmethod
    def create(doc):
        assert doc.get("table")
        assert doc.get("candidate")
        table = Tables.create(doc.get("table"))
        candidate = Candidate.create(doc.get("candidate"))
        return Results(
            number_votes=doc.get("number_votes"),
            table=table,
            candidate=candidate,

        )


class ResultsDoesNotExist(ElementDoesNotExist):
    pass
