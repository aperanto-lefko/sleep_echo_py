from sqlalchemy.orm import Session
from sqlmodel import select
from typing import List, Optional
from models.sleep_data import SleepData



class SleepDataRepository:
    """Репозиторий для работы с данными о сне"""

    def __init__(self, session: Session):
        self.session = session

    def add_sleep_data(self, data: SleepData) -> SleepData:
        """Добавление записи о сне"""
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        return data

    def remove_sleep_data(self, data: SleepData) -> bool:
        """Удаление записи о сне"""
        self.session.delete(data)
        self.session.commit()
        return True

    def find_by_id(self, id: int) -> Optional[SleepData]:
        """Поиск записи по ID"""
        return self.session.get(SleepData, id)

    def update_sleep_data(self, data: SleepData) -> bool:
        """Обновление записи о сне"""
        existing_data = self.session.get(SleepData, data.id)
        if not existing_data:
            return False

        # Обновляем только измененные поля
        for key, value in data.dict(exclude_unset=True).items():
            setattr(existing_data, key, value)

        self.session.commit()
        return True

    def get_sleep_data_with_parameters(
            self,
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
            stress_end: int = 0
    ) -> List[SleepData]:
        """Получение данных о сне с фильтрацией по параметрам"""

        # Проверка на пустые параметры
        all_parameters_empty = all([
            respondent_id == 0,
            sl_start_time_start == 0 and sl_start_time_end == 0,
            sl_end_time_start == 0 and sl_end_time_end == 0,
            sl_total_time_start == 0 and sl_total_time_end == 0,
            sl_quality_start == 0 and sl_quality_end == 0,
            exercise_start == 0 and exercise_end == 0,
            coffee_start == 0 and coffee_end == 0,
            screen_time_start == 0 and screen_time_end == 0,
            work_time_start == 0 and work_time_end == 0,
            productivity_start == 0 and productivity_end == 0,
            mood_start == 0 and mood_end == 0,
            stress_start == 0 and stress_end == 0
        ])
        if all_parameters_empty:
            # Если все параметры пустые - возвращаем все данные с сортировкой по ID
            query = select(SleepData).order_by(SleepData.id)
            result = self.session.exec(query)
            return result.all()

        query = select(SleepData)

        if not all_parameters_empty:
            if respondent_id > 0:
                query = query.where(SleepData.person_id == respondent_id)

            # Фильтрация по времени начала сна
            if sl_start_time_start > 0 and sl_start_time_end > 0:
                query = query.where(SleepData.sleep_start_time.between(sl_start_time_start, sl_start_time_end))
            elif sl_start_time_start > 0:
                query = query.where(SleepData.sleep_start_time >= sl_start_time_start)
            elif sl_start_time_end > 0:
                query = query.where(SleepData.sleep_start_time <= sl_start_time_end)

            # Фильтрация по времени окончания сна
            if sl_end_time_start > 0 and sl_end_time_end > 0:
                query = query.where(SleepData.sleep_end_time.between(sl_end_time_start, sl_end_time_end))
            elif sl_end_time_start > 0:
                query = query.where(SleepData.sleep_end_time >= sl_end_time_start)
            elif sl_end_time_end > 0:
                query = query.where(SleepData.sleep_end_time <= sl_end_time_end)

            # Фильтрация по общему времени сна
            if sl_total_time_start > 0 and sl_total_time_end > 0:
                query = query.where(SleepData.total_sleep_hours.between(sl_total_time_start, sl_total_time_end))
            elif sl_total_time_start > 0:
                query = query.where(SleepData.total_sleep_hours >= sl_total_time_start)
            elif sl_total_time_end > 0:
                query = query.where(SleepData.total_sleep_hours <= sl_total_time_end)

            # Фильтрация по качеству сна
            if sl_quality_start > 0 and sl_quality_end > 0:
                query = query.where(SleepData.sleep_quality.between(sl_quality_start, sl_quality_end))
            elif sl_quality_start > 0:
                query = query.where(SleepData.sleep_quality >= sl_quality_start)
            elif sl_quality_end > 0:
                query = query.where(SleepData.sleep_quality <= sl_quality_end)

            # Фильтрация по времени упражнений
            if exercise_start > 0 and exercise_end > 0:
                query = query.where(SleepData.exercise_minutes.between(exercise_start, exercise_end))
            elif exercise_start > 0:
                query = query.where(SleepData.exercise_minutes >= exercise_start)
            elif exercise_end > 0:
                query = query.where(SleepData.exercise_minutes <= exercise_end)

            # Фильтрация по потреблению кофеина
            if coffee_start > 0 and coffee_end > 0:
                query = query.where(SleepData.caffeine_intake_mg.between(coffee_start, coffee_end))
            elif coffee_start > 0:
                query = query.where(SleepData.caffeine_intake_mg >= coffee_start)
            elif coffee_end > 0:
                query = query.where(SleepData.caffeine_intake_mg <= coffee_end)

            # Фильтрация по времени у экрана
            if screen_time_start > 0 and screen_time_end > 0:
                query = query.where(SleepData.screen_time.between(screen_time_start, screen_time_end))
            elif screen_time_start > 0:
                query = query.where(SleepData.screen_time >= screen_time_start)
            elif screen_time_end > 0:
                query = query.where(SleepData.screen_time <= screen_time_end)

            # Фильтрация по рабочему времени
            if work_time_start > 0 and work_time_end > 0:
                query = query.where(SleepData.work_hours.between(work_time_start, work_time_end))
            elif work_time_start > 0:
                query = query.where(SleepData.work_hours >= work_time_start)
            elif work_time_end > 0:
                query = query.where(SleepData.work_hours <= work_time_end)

            # Фильтрация по продуктивности
            if productivity_start > 0 and productivity_end > 0:
                query = query.where(SleepData.productivity_score.between(productivity_start, productivity_end))
            elif productivity_start > 0:
                query = query.where(SleepData.productivity_score >= productivity_start)
            elif productivity_end > 0:
                query = query.where(SleepData.productivity_score <= productivity_end)

            # Фильтрация по настроению
            if mood_start > 0 and mood_end > 0:
                query = query.where(SleepData.mood_score.between(mood_start, mood_end))
            elif mood_start > 0:
                query = query.where(SleepData.mood_score >= mood_start)
            elif mood_end > 0:
                query = query.where(SleepData.mood_score <= mood_end)

            # Фильтрация по уровню стресса
            if stress_start > 0 and stress_end > 0:
                query = query.where(SleepData.stress_level.between(stress_start, stress_end))
            elif stress_start > 0:
                query = query.where(SleepData.stress_level >= stress_start)
            elif stress_end > 0:
                query = query.where(SleepData.stress_level <= stress_end)

            # Сортировка и выполнение запроса
        query = query.order_by(SleepData.id)
        result = self.session.exec(query)
        return result.all()