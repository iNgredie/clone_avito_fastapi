from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from ..models.advertisment import AdvertismentStatus


class AdvertismentBase(BaseModel):
    name: str
    city_id: int
    description: Optional[str]
    published_at: datetime
    created_at: datetime
    updated_at: datetime
    price: Decimal
    view: int
    status: AdvertismentStatus


class Advertisment(AdvertismentBase):
    id: int

    class Config:
        orm_mode = True


class AdvertismentCreate(AdvertismentBase):
    pass


class AdvertismentUpdate(AdvertismentBase):
    pass
