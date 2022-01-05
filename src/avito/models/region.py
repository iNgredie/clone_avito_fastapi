from sqlalchemy import Column, Integer, String

from ..models.base import Base


class Region(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
