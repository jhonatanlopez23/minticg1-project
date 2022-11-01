from bson import ObjectId

from controllers.abstract import CRUDController
from models.results import Results, ResultsDoesNotExist
from models.candidates import Candidate, CandidateDoesNotExist
from models.tables import Tables, TableDoesNotExist
from repositories.results import ResultsRepository
from repositories.candidates import CandidateRepository
from repositories.tables import TablesRepository


class ResultsController(CRUDController):

    def __init__(self):
        self.repository = ResultsRepository(
            Results,
            ResultsDoesNotExist
        )
        self.r_candidate = CandidateRepository(
            Candidate,
            CandidateDoesNotExist
        )
        self.r_table = TablesRepository(
            Tables,
            TableDoesNotExist
        )

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id_element):
        return self.repository.get_by_id(id_element)

    def create(self, content):
        doc_tables = content.get("table", {})
        doc_candidates = content.get("candidate", {})
        content["table"] = self.r_table.get_by_id(
            doc_tables.get("id")).to_json()
        content["candidate"] = self.r_candidate.get_by_id(
            doc_candidates.get("id")).to_json()
        return self.repository.save(
            item=Results.create(content)
        )

    def update(self, id_element, content):
        element = self.get_by_id(id_element)
        element.number_votes = content["number_votes"]

        doc_tables = content.get("tables", {})
        doc_candidates = content.get("candidates", {})
        element.table = self.r_table.get_by_id(doc_tables.get("id"))
        element.candidate = self.r_candidate.get_by_id(
            doc_candidates.get("id"))
        return self.repository.save(element)

    def delete(self, id_element):
        element = self.get_by_id(id_element)
        return self.repository.delete(element)

    def count(self):
        return self.repository.count()
