from controllers.abstract import CRUDController
from models.candidate import Candidate, CandidateDoesNotExist

from repositories.candidate import CandidateRepository


class candidatesController(CRUDController):

    def __init__(self):
        self.repository = CandidateRepository(
            model=Candidate,
            does_not_exist=CandidateDoesNotExist
        )

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id_candidate):
        return self.repository.get_by_id(id_candidate)

    def create(self, content):
        created = Candidate(
            identification=content["identification"],
            first_name=content["first_name"],
            last_name=content["last_name"],
            email=content["email"],
            resolution_number=["resolution_number"]

        )
        return self.repository.save(created)

    def update(self, id_candidate, content):
        candidate = self.get_by_id(id_candidate)
        candidate.identification = content["identification"]
        candidate.first_name = content["first_name"]
        candidate.last_name = content["last_name"]
        candidate.email = content["email"]
        candidate.resolution_number = content["resolution_number"]
        return self.repository.save(candidate)

    def delete(self, id_candidate):
        candidate = self.get_by_id(id_candidate)
        return self.repository.delete(candidate)

    def count(self):
        return self.repository.count()