from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from ..database import get_session
from ..schemas.advertisment import AdvertismentCreate, AdvertismentUpdate


class AdvertismentService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, advertisment_id: int) -> models.Advertisment:
        advertisment = (
            self.session
            .query(models.Advertisment)
            .filter_by(id=advertisment_id)
            .first
        )
        if not advertisment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return advertisment

    def get_list(self) -> List[models.Advertisment]:
        query = (
            self.session
            .query(models.Advertisment)
        )
        return query.all()

    def get(self, advertisment_id: int) -> models.Advertisment:
        return self._get(advertisment_id)

    def create(self, advertisment_data: AdvertismentCreate) -> models.Advertisment:
        advertisment = models.Advertisment(**advertisment_data.dict())
        self.session.add(advertisment)
        self.session.commit()
        return advertisment

    def update(self, advertisment_id: int, advertisment_data: AdvertismentUpdate) -> models.Advertisment:
        advertisment = self._get(advertisment_id)
        for field, value in advertisment_data:
            setattr(advertisment, field, value)
        self.session.commit()
        return advertisment

    def delete(self, advertisment_id: int) -> None:
        advertisment = self._get(advertisment_id)
        self.session.delete(advertisment)
        self.session.commit()
