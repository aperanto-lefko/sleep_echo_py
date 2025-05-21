from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from models.sleep_data import SleepData

class Respondent(SQLModel, table=True):
    __tablename__ = "respondents"
    __table_args__ = {"schema": "sleep"}
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str
    gender: str
    country: str
    age: int


