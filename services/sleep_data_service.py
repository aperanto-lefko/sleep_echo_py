from datetime import datetime
from typing import List
from sqlalchemy.exc import NoResultFound
from contextlib import contextmanager
from models.sleep_data import SleepData


class SleepDataService:
    def __init__(self, sleep_data_repository, respondent_service):
        self._sleep_data_repository = sleep_data_repository
        self._r_service = respondent_service

    @contextmanager
    def _transaction(self):
        """Контекстный менеджер для транзакций"""
        try:
            yield
            self._sleep_data_repository.session.commit()
        except Exception:
            self._sleep_data_repository.session.rollback()
            raise

    def add_sleep_data(self,
                       person_id: int,
                       sleep_start_time: float,
                       sleep_end_time: float,
                       total_sleep_hours: float,
                       sleep_quality: int,
                       exercise_minutes: int,
                       caffeine_intake_mg: int,
                       screen_time: int,
                       work_hours: float,
                       productivity_score: int,
                       mood_score: int,
                       stress_level: int) -> SleepData:
        """
        Добавление данных о сне
        """
        # Проверяем существование респондента
        self._r_service.search_resp_by_id(person_id)

        new_sleep_data = SleepData(
            person_id=person_id,
            sleep_date=datetime.now().date(),
            sleep_start_time=sleep_start_time,
            sleep_end_time=sleep_end_time,
            total_sleep_hours=total_sleep_hours,
            sleep_quality=sleep_quality,
            exercise_minutes=exercise_minutes,
            caffeine_intake_mg=caffeine_intake_mg,
            screen_time_before_bed=screen_time,
            work_hours=work_hours,
            productivity_score=productivity_score,
            mood_score=mood_score,
            stress_level=stress_level
        )

        return self._sleep_data_repository.add_sleep_data(new_sleep_data)

    def update_sleep_data(self,
                          data_id: int,
                          person_id: int,
                          sleep_start_time: float,
                          sleep_end_time: float,
                          total_sleep_hours: float,
                          sleep_quality: int,
                          exercise_minutes: int,
                          caffeine_intake_mg: int,
                          screen_time: int,
                          work_hours: float,
                          productivity_score: int,
                          mood_score: int,
                          stress_level: int) -> bool:
        """
        Обновление данных о сне с транзакцией
        """
        with self._transaction():
            old_data = self.get_sleep_data_by_id(data_id)

            # Обновляем только переданные параметры
            if person_id is not None:
                self._r_service.search_resp_by_id(person_id)
                old_data.person_id = person_id
            if sleep_start_time is not None:
                old_data.sleep_start_time = sleep_start_time
            if sleep_end_time is not None:
                old_data.sleep_end_time = sleep_end_time
            if total_sleep_hours is not None:
                old_data.total_sleep_hours = total_sleep_hours
            if sleep_quality is not None:
                old_data.sleep_quality = sleep_quality
            if exercise_minutes is not None:
                old_data.exercise_minutes = exercise_minutes
            if caffeine_intake_mg is not None:
                old_data.caffeine_intake_mg = caffeine_intake_mg
            if screen_time is not None:
                old_data.screen_time_before_bed = screen_time
            if work_hours is not None:
                old_data.work_hours = work_hours
            if productivity_score is not None:
                old_data.productivity_score = productivity_score
            if mood_score is not None:
                old_data.mood_score = mood_score
            if stress_level is not None:
                old_data.stress_level = stress_level

            return self._sleep_data_repository.update_sleep_data(old_data)

    def remove_sleep_data_by_id(self, id: int) -> bool:
        """
        Удаление данных о сне по ID
        """
        data = self.get_sleep_data_by_id(id)
        return self._sleep_data_repository.remove_sleep_data(data)

    def get_sleep_data_by_id(self, id: int) -> SleepData:
        """
        Получение данных о сне по ID
        """
        data = self._sleep_data_repository.find_by_id(id)
        if not data:
            raise NoResultFound(f"Данные с ID: {id} не найдены")
        return data

    def get_sleep_data_with_parameters(self,
                                       respondent_id: int = 0,
                                       sl_start_time_start: float = 0,
                                       sl_start_time_end: float = 0,
                                       sl_end_time_start: float = 0,
                                       sl_end_time_end: float = 0,
                                       sl_total_time_start: float = 0,
                                       sl_total_time_end: float = 0,
                                       sl_quality_start: int = 0,
                                       sl_quality_end: int = 0,
                                       exercise_start: int = 0,
                                       exercise_end: int = 0,
                                       coffee_start: int = 0,
                                       coffee_end: int = 0,
                                       screen_time_start: int = 0,
                                       screen_time_end: int = 0,
                                       work_time_start: float = 0,
                                       work_time_end: float = 0,
                                       productivity_start: int = 0,
                                       productivity_end: int = 0,
                                       mood_start: int = 0,
                                       mood_end: int = 0,
                                       stress_start: int = 0,
                                       stress_end: int = 0) -> List[SleepData]:
        """
        Получение данных о сне с фильтрами
        """
        return self._sleep_data_repository.get_sleep_data_with_parameters(
            respondent_id=respondent_id,
            sl_start_time_start=sl_start_time_start,
            sl_start_time_end=sl_start_time_end,
            sl_end_time_start=sl_end_time_start,
            sl_end_time_end=sl_end_time_end,
            sl_total_time_start=sl_total_time_start,
            sl_total_time_end=sl_total_time_end,
            sl_quality_start=sl_quality_start,
            sl_quality_end=sl_quality_end,
            exercise_start=exercise_start,
            exercise_end=exercise_end,
            coffee_start=coffee_start,
            coffee_end=coffee_end,
            screen_time_start=screen_time_start,
            screen_time_end=screen_time_end,
            work_time_start=work_time_start,
            work_time_end=work_time_end,
            productivity_start=productivity_start,
            productivity_end=productivity_end,
            mood_start=mood_start,
            mood_end=mood_end,
            stress_start=stress_start,
            stress_end=stress_end
        )