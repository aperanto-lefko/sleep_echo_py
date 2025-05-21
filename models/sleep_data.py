from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import Optional

from models.respondent import Respondent


class SleepData(SQLModel, table=True):
    __tablename__ = "sleep_data"
    __table_args__ = {"schema": "sleep"}

    id: Optional[int] = Field(default=None, primary_key=True, sa_column_kwargs={"name": "id"})
    sleep_date: date = Field(sa_column_kwargs={"name": "date"})
    person_id: int = Field(foreign_key="sleep.respondents.id", sa_column_kwargs={"name": "person_id"})

    respondent: Optional["Respondent"] = Relationship()


    sleep_start_time: float
    sleep_end_time: float
    total_sleep_hours: float
    sleep_quality: int
    exercise_minutes: int
    caffeine_intake_mg: int
    screen_time_before_bed: int
    work_hours: float
    productivity_score: int
    mood_score: int
    stress_level: int