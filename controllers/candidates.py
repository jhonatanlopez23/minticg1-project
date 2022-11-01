from controllers.abstract import CRUDController
from models.party import Party, PartyDoesNotExist
from models.candidates import Candidate, CandidateDoesNotExist
from repositories.party import PartyRepository
from repositories.candidates import CandidateRepository


class CandidatesController(CRUDController):
    def __init__(self):
        self.repository = CandidateRepository(
            Candidate,
            CandidateDoesNotExist
        )
        self.repo_p = PartyRepository(
            Party,
            PartyDoesNotExist
        )

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id_element):
        return self.repository.get_by_id(id_element)

    def create(self, content):
        doc_party = content.get("party", {})
        party = self.repo_p.get_by_id(doc_party.get("id"))
        content["party"] = party.to_json()
        return self.repository.save(
            item=Candidate.create(content)
        )

    def update(self, id_element, content):
        element = self.get_by_id(id_element)
        element.resolution_number = content["resolution_number"]
        element.names = content["names"]
        element.last_names = content["last_names"]
        element.identification = content["identification"]
        return self.repository.save(element)

    def delete(self, id_element):
        element = self.get_by_id(id_element)
        return self.repository.delete(element)

    def count(self):
        return self.repository.count()

    def set_party_to_candidate(self, id_candidate, id_party):
        candidate = self.repository.get_by_id(id_candidate)
        party = self.repo_d.get_by_id(id_party)
        candidate.party = party
        return self.repository.save(candidate)
