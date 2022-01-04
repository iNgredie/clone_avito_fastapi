from typing import Optional

from pydantic import BaseModel


class BaseUser(BaseModel):
    email: str
    username: str


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int
    name: str
    surname: str
    patronymic: Optional[str]
    role: str
    phone: str
    status: str

    class Config:
        orm_mode = True

