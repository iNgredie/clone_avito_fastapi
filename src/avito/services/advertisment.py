from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from ..database import get_session
from ..schemas.advertisment import AdvertismentCreate, AdvertismentUpdate


class AdvertismentService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int, advertisment_id: int) -> models.Advertisment:
        advertisment = (
            self.session.query(models.Advertisment)
            .filter_by(
                id=advertisment_id,
                user_id=user_id,
            )
            .first
        )
        if not advertisment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return advertisment

    def get_list(self, user_id: int) -> List[models.Advertisment]:
        query = self.session.query(models.Advertisment).filter_by(
            user_id=user_id, status=models.AdvertismentStatus.ACTIVE
        )
        return query.all()

    def get(self, user_id: int, advertisment_id: int) -> models.Advertisment:
        return self._get(user_id, advertisment_id)

    def create(
        self, user_id: int, advertisment_data: AdvertismentCreate
    ) -> models.Advertisment:
        advertisment = models.Advertisment(
            **advertisment_data.dict(),
            user_id=user_id,
        )
        self.session.add(advertisment)
        self.session.commit()
        return advertisment

    def update(
        self, user_id: int, advertisment_id: int, advertisment_data: AdvertismentUpdate
    ) -> models.Advertisment:
        advertisment = self._get(user_id, advertisment_id)
        for field, value in advertisment_data:
            setattr(advertisment, field, value)
        self.session.commit()
        return advertisment

    def delete(self, user_id: int, advertisment_id: int) -> None:
        advertisment = self._get(user_id, advertisment_id)
        self.session.delete(advertisment)
        self.session.commit()
