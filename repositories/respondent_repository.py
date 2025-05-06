"""Модуль с репозиторием для работы с респондентами."""
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

    def create(self,first_name: str,last_name: str,email: str,gender: str,country: str,age: int):
        """Создать нового респондента."""
        respondent = Respondent(first_name=first_name,
                                last_name=last_name,
                                email=email,
                                gender=gender,
                                country=country,
                                age=age)
        self.session.add(respondent)
        self.session.commit()
        self.session.refresh(respondent)
        return respondent

    def update(self,respondent_id: int, **kwargs):
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
        respondent=self.session.get(Respondent, respondent_id)
        if respondent:
            self.session.delete(respondent)
            self.session.commit()
