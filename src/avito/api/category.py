from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.openapi.models import Response

from ..schemas.category import Category, CategoryCreate, CategoryUpdate
from ..services.category import CategoryService

router = APIRouter(
    prefix='/category',
    tags=['category'],
)


@router.get('/', response_model=List[Category])
def get_categories(
    service: CategoryService = Depends(),
):
    return service.get_list()


@router.post('/', response_model=Category)
def create_category(
    category_data: CategoryCreate,
    service: CategoryService = Depends(),
):
    return service.create(category_data=category_data)


@router.get('/{category_id}', response_model=Category)
def get_category(
    category_id: int,
    service: CategoryService = Depends(),
):
    return service.get(category_id=category_id)


@router.put('/{category_id}', response_model=Category)
def update_category(
    category_id: int,
    category_data: CategoryUpdate,
    service: CategoryService = Depends(),
):
    return service.update(
        category_id=category_id,
        category_data=category_data,
    )


@router.delete('/{category_id}', response_model=Category)
def delete_category(
    category_id: int,
    service: CategoryService = Depends(),
):
    service.delete(category_id=category_id,)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
