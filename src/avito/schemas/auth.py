from typing import Optional

from pydantic import BaseModel

from avito.models import UserStatus


class BaseUser(BaseModel):
    email: str
    username: str


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int
    name: Optional[str]
    surname: Optional[str]
    patronymic: Optional[str]
    role: Optional[str]
    phone: Optional[str]
    status: UserStatus

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
