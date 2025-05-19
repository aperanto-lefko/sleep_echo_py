"""Модуль с репозиторием для работы с респондентами."""
from sqlalchemy import func, false
from sqlmodel import Session, select
from models.respondent import Respondent


class RespondentRepository:
    """Репозиторий для операций с моделью Respondent."""
    def __init__(self,session:Session):
        """Инициализация сессии базы данных."""
        self.session=session

    def get_all(self):
        """Получить всех респондентов."""
        return self.session.exec(select(Respondent)).all()


    def create(self, **kwargs):
        """Создать нового респондента."""
        respondent = Respondent(**kwargs)
        self.session.add(respondent)
        self.session.commit()
        self.session.refresh(respondent)
        return respondent

    def update(self,respondent_id, **kwargs):
        """Обновить данные респондента по ID."""
        respondent = self.session.get(Respondent, respondent_id)
        if not respondent:
            return None
        for key, value in kwargs.items():
            setattr(respondent, key, value)
        self.session.commit()
        self.session.refresh(respondent)
        return respondent

    def delete(self, respondent_id: int):
        """Удалить респондента по ID."""
        respondent=self.search_resp_by_id(respondent_id)
        if respondent:
            self.session.delete(respondent)
            self.session.commit()

    def search_resp_by_last_name(self, last_name):
        """Поиск респондента по фамилии"""
        query = select(Respondent).where(
            func.lower(Respondent.last_name).startswith(last_name.lower()))
        return self.session.exec(query).all()

    def search_resp_by_id(self, resp_id):
        return self.session.get(Respondent, resp_id)

    def delete_resp_by_id(self, resp_id):
        respondent = self.search_resp_by_id(resp_id)
        if not respondent:
            return False
        self.session.delete(respondent)
        self.session.commit()
        return True
