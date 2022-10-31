from models.abstract import AbstractModel, ElementDoesNotExist


class Tables(AbstractModel):
    COLLECTION_NAME = "tables"
    _id = None
    table_number = None
    cedulas_inscritas = None

    def __init__(
        self,
        table_number,
        cedulas_inscritas,
        _id=None,
    ):
        super().__init__(_id)
        self.table_number = table_number
        self.cedulas_inscritas = cedulas_inscritas

    def prepare_to_save(self):
        return {
            "table_number": self.table_number,
            "cedulas_inscritas": self.cedulas_inscritas
        }

    def to_json(self):
        return self.__dict__

    @staticmethod
    def create(doc):
        return Tables(
            table_number=doc["table_number"],
            cedulas_inscritas=doc["cedulas_inscritas"],
            _id=str(doc["_id"]) if doc.get("_id") else None
        )


class TableDoesNotExist(ElementDoesNotExist):
    pass
