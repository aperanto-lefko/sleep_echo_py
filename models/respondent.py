from typing import Optional

from sqlmodel import SQLModel,Field


class Respondent(SQLModel, table=True):
    __tablename__ = "respondents"
    __table_args__= {"schema":"sleep"}
    id: Optional[int]=Field(default=None,primary_key=True)
    first_name:str =Field(sa_column_kwargs={"name": "first_name"})
    last_name: str = Field(sa_column_kwargs={"name": "last_name"})
    email:str=Field(index=True, unique=True, sa_column_kwargs={"name": "email"})
    gender: str = Field(sa_column_kwargs={"name": "gender"})
    country: str =  Field(sa_column_kwargs={"name": "country"})
    age: int =  Field(sa_column_kwargs={"name": "age"})
