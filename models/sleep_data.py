from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import Optional


class SleepData(SQLModel, table=True):
    __tablename__ = "sleep_data"
    __table_args__ = {"schema": "sleep"}

    id: Optional[int] = Field(default=None, primary_key=True, sa_column_kwargs={"name": "id"})
    date: date = Field(sa_column_kwargs={"name": "date"})
    person_id: int = Field(foreign_key="sleep.respondents.id", sa_column_kwargs={"name": "person_id"})

    respondent: Optional["Respondent"] = Relationship()

    sleep_start_time: float = Field(sa_column_kwargs={"name": "sleep_start_time"})
    sleep_end_time: float = Field(sa_column_kwargs={"name": "sleep_end_time"})
    total_sleep_hours: float = Field(sa_column_kwargs={"name": "total_sleep_hours"})
    sleep_quality: int = Field(sa_column_kwargs={"name": "sleep_quality"})
    exercise_minutes: int = Field(sa_column_kwargs={"name": "exercise_minutes"})
    caffeine_intake_mg: int = Field(sa_column_kwargs={"name": "caffeine_intake_mg"})
    screen_time_before_bed: int = Field(sa_column_kwargs={"name": "screen_time_before_bed"})
    work_hours: float = Field(sa_column_kwargs={"name": "work_hours"})
    productivity_score: int = Field(sa_column_kwargs={"name": "productivity_score"})
    mood_score: int = Field(sa_column_kwargs={"name": "mood_score"})
    stress_level: int = Field(sa_column_kwargs={"name": "stress_level"})