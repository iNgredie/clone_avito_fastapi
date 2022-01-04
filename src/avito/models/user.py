from sqlalchemy import Column, Integer, String, Text

from ..models.base import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(length=255), unique=True)
    username = Column(String(length=255), unique=True)
    password_hash = Column(Text)
    name = Column(String(length=255))
    surname = Column(String(length=255))
    patronymic = Column(String(length=255), nullable=True)
    phone = Column(String(length=255))
    status = Column(String(length=255))

