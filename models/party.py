from models.abstract import AbstractModel, ElementDoesNotExist


class Party(AbstractModel):
    COLLECTION_NAME = "party"

    name = None
    slogan = None

    def __init__(
        self,
        name,
        slogan,
        _id=None,
    ):

        super().__init__(_id)
        self.name = name
        self.slogan = slogan

    def prepare_to_save(self):
        return {
            "name": self.name,
            "slogan": self.slogan
        }

    def to_json(self):
        return self.__dict__

    @staticmethod
    def create(doc):
        return Party(
            name=doc["name"],
            slogan=doc["slogan"],
            _id=str(doc["_id"]) if doc.get("_id") else None,
        )


class PartyDoesNotExist(ElementDoesNotExist):
    pass