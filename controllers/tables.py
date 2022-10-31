
from controllers.abstract import CRUDController
from models.tables import Tables, TableDoesNotExist
from repositories.tables import TablesRepository


class TablesController(CRUDController):
    def __init__(self):
        self.repository = TablesRepository(
            model=Tables,
            does_not_exist=TableDoesNotExist
        )

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id_table):
        return self.repository.get_by_id(id_table)

    def create(self, content):
        created = Tables(
            table_number=content["table_number"],
            cedulas_inscritas=content["cedulas_inscritas"],
        )
        return self.repository.save(created)

    def update(self, id_table, contend):
        table = self.get_by_id(id_table)
        #table.table_number = contend["table_number"]
        table.cedulas_inscritas = contend["cedulas_inscritas"]
        return self.repository.save(table)

    def delete(self, id_table):
        table = self.get_by_id(id_table)
        return self.repository.delete(table)

    def count(self):
        return self.repository.count()
