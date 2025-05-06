# User CRUD-операции
from repositories.respondent_repository import RespondentRepository


class RespondentService:
    def __init__(self, repository:RespondentRepository):
        self.repository=repository

    def get_respondents(self):
        return self.repository.get_all()

    def add_respondent(self, name:str, email:str, phone:str):
        return self.repository.create(name,email, phone)

    def update_respondent(self, respondent_id:int, **kwargs):
        return self.repository.update(respondent_id, **kwargs)

    def remove_respondent(self, respondent_id:int):
        return self.repository.delete(respondent_id)