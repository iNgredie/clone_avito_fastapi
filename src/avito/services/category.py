from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from ..database import get_session
from ..schemas.category import CategoryCreate, CategoryUpdate


class CategoryService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, category_id: int) -> models.Category:
        category = (
            self.session.query(models.Category)
            .filter_by(
                id=category_id,
            )
            .first
        )
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return category

    def get_list(self) -> List[models.Category]:
        query = self.session.query(models.Category)
        return query.all()

    def get(self, category_id: int) -> models.Category:
        return self._get(category_id)

    def create(self, category_data: CategoryCreate) -> models.category:
        category = models.Category(
            **category_data.dict(),
        )
        self.session.add(category)
        self.session.commit()
        return category

    def update(
        self, category_id: int, category_data: CategoryUpdate
    ) -> models.category:
        category = self._get(category_id)
        for field, value in category_data:
            setattr(category, field, value)
        self.session.commit()
        return category

    def delete(self, category_id: int) -> None:
        category = self._get(category_id)
        self.session.delete(category)
        self.session.commit()
