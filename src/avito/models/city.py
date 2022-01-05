from sqlalchemy import Column, ForeignKey, Integer, String

from ..models.base import Base


class City(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
    region_id = Column(
        Integer, ForeignKey('region.id', name='fk_city_region_region_id', ondelete='CASCADE'),
        nullable=True
    )
