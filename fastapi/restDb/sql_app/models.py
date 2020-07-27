from sqlalchemy import Column, Enum as SqlEnum, Integer, String, Date
from sqlalchemy.orm import relationship
from enum import Enum

from .database import Base


class Status(Enum):
    ALIVE = "ALIVE"
    DEAD = "DEAD"


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    birth = Column(Date)
    status = Column(SqlEnum(Status))
