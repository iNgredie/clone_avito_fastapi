import enum

from sqlalchemy import Column, Integer, String, Text

from ..models.base import Base


class UserStatus(str, enum.Enum):
    ACTIVE = 'active'
    BLOCKED = 'blocked'
    WAIT = 'wait'


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(length=255), unique=True)
    username = Column(String(length=255), unique=True)
    password_hash = Column(Text)
    name = Column(String(length=255), nullable=True)
    role = Column(String(length=255), nullable=True)
    surname = Column(String(length=255), nullable=True)
    patronymic = Column(String(length=255), nullable=True)
    phone = Column(String(length=255), nullable=True)
    status = Column(String(length=255), default=UserStatus.ACTIVE)
