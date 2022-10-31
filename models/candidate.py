from models.abstract import AbstractModel, ElementDoesNotExist


class Candidate(AbstractModel):
    COLLECTION_NAME = "votes"

    identificacion = None
    first_name = None
    last_name = None
    email = None
    resolution_number=None

    def __init__(
            self,
            identificacion,
            first_name,
            last_name,
            email,
            resolution_number,
            _id=None,
    ):
        super().__init__(_id)
        self.identificacion = identificacion
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.resolution_number=resolution_number

    def prepare_to_save(self):
        return {
            "identificacion": self.identificacion,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "resolution_number": self.resolution_number
        }

    def to_json(self):
        return self.__dict__

    @staticmethod
    def create(doc):
        """
        Patron Factory
        """
        return Candidate(
            identificacion=doc["identificacion"],
            last_name=doc["last_name"],
            first_name=doc["first_name"],
            email=doc["email"],
            resolution_number=doc["resolution_number"]
            _id=str(doc["_id"]) if doc.get("_id") else None,
        )


class CandidateDoesNotExist(ElementDoesNotExist):
    pass