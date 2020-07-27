from datetime import date
from pydantic import BaseModel
from .models import Status


class PersonBase(BaseModel):
    name: str
    birth: date
    status: Status


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    id: int

    class Config:
        orm_mode = True
