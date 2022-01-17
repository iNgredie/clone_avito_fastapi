import enum
from datetime import datetime

from sqlalchemy import (
    DECIMAL, Column, DateTime, Enum, ForeignKey, Integer, String, Text
)

from ..models.base import Base


class AdvertismentStatus(enum.Enum):
    DRAFT = 'draft'
    ON_MODERATION = 'on_moderation'
    REJECTED = 'rejected'
    SOLD = 'sold'
    ACTIVE = 'active'


class Advertisment(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
    user_id = Column(
        Integer, ForeignKey('user.id', name='fk_advertisment_user_user_id', ondelete='CASCADE')
    )
    category_id = Column(
        Integer, ForeignKey('category.id', name='fk_advertisment_category_category_id', ondelete='CASCADE')
    )
    city_id = Column(
        Integer, ForeignKey('city.id', name='fk_advertisment_city_city_id', ondelete='CASCADE'),
        nullable=True
    )
    description = Column(Text)
    published_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.utcnow, default=datetime.utcnow)
    price = Column(DECIMAL)
    view = Column(Integer, default=0)
    status = Column(Enum(AdvertismentStatus))
