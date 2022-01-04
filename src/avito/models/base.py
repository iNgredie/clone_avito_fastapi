import re

from sqlalchemy.orm import declared_attr


class Base(object):
    def __init__(self, *args, **kwargs):
        ...

    @declared_attr
    def __tablename__(cls):
        return cls.camel_to_snake(cls.__name__)

    @staticmethod
    def camel_to_snake(name: str) -> str:
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

