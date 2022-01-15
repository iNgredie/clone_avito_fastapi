from sqlalchemy import Column, Integer, String, Text

from ..models.base import Base


class Category(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255))
    slug = Column(String(length=255), unique=True)
    description = Column(Text, nullable=True)
