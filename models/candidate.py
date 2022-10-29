from models.abstract import Abstract

class Candidate(Abstract):
    _id: None
    identification:None
    first_name:None
    last_name:None
    email:None
    political_party:None
    number_political_party:None

    def __init__(self, _id, identification, first_name, last_name, email, political_party, number_political_party):
        
        super().__init__(_id)
        self.identification=identification
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.political_party=political_party
        self.number_political_party=number_political_party
        