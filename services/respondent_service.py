# User CRUD-операции
from exception.exceptions import RespondentNotFoundException
from repositories.respondent_repository import RespondentRepository
import logging

logger = logging.getLogger(__name__)

class RespondentService:
    def __init__(self, repository:RespondentRepository):
        self.repository=repository
        logger.info("RespondentService initialized")

    def get_respondents(self):
        logger.info("Fetching all respondents")
        return self.repository.get_all()

    def add_respondent(self, **data):
        logger.info(f"Adding respondent: {data.get('first_name')} {data.get('last_name')}, Email: {data.get('email')}")
        return self.repository.create(**data)


    def remove_respondent(self, respondent_id:int):
        logger.info(f"Removing respondent with ID {respondent_id}")
        return self.repository.delete(respondent_id)

    def search_resp_by_last_name(self,last_name):
        logger.info(f"Searching respondent(s) by last name: {last_name}")
        return self.repository.search_resp_by_last_name(last_name)

    def search_resp_by_id(self, resp_id):
        logger.info(f"Searching respondent by id: {resp_id}")
        respondent = self.repository.search_resp_by_id(resp_id)
        if not respondent:
            raise RespondentNotFoundException(f"Респондент с id {resp_id} не найден")
        return respondent

    def update_respondent(self, resp_id, **data):
        logger.info(f"Update respondent: id: {resp_id}, with data {data}")
        respondent = self.repository.update(resp_id, **data)
        if not respondent:
            raise RespondentNotFoundException(f"Респондент с id {resp_id} не найден")
        return respondent
    def delete_resp_by_id(self,resp_id):
        logger.info(f"Delete respondent with id: {resp_id}")
        result = self.repository.delete_resp_by_id(resp_id)
        if not result:
            raise RespondentNotFoundException(f"Респондент с id {resp_id} не найден")
        return result
