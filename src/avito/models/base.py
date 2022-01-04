import re

from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declared_attr


@as_declarative()
class Base(object):
    def __init__(self, *args, **kwargs):
        ...

    @declared_attr
    def __tablename__(self):
        return self.camel_to_snake(self.__name__)

    @staticmethod
    def camel_to_snake(name: str) -> str:
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
