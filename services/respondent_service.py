# User CRUD-операции
from repositories.respondent_repository import RespondentRepository


class RespondentService:
    def __init__(self, repository:RespondentRepository):
        self.repository=repository

    def get_respondents(self):
        return self.repository.get_all()

    def add_respondent(self, first_name:str, last_name: str, email:str, gender:str, country:str, age: int):
        return self.repository.create(first_name,last_name, email, gender, country, age)

    def update_respondent(self, respondent_id:int, **kwargs):
        return self.repository.update(respondent_id, **kwargs)

    def remove_respondent(self, respondent_id:int):
        return self.repository.delete(respondent_id)