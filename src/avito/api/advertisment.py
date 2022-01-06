from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.openapi.models import Response

from ..schemas.advertisment import (
    Advertisment, AdvertismentCreate, AdvertismentUpdate
)
from ..services.advertisment import AdvertismentService

router = APIRouter(
    prefix='/advertisment'
)


@router.get('/', response_model=List[Advertisment])
def get_advertisments(
    service: AdvertismentService = Depends(),
):
    return service.get_list()


@router.post('/', response_model=Advertisment)
def create_advertisment(
    advertisment_data: AdvertismentCreate,
    service: AdvertismentService = Depends(),
):
    return service.create(advertisment_data)


@router.get('/{advertisment_id}', response_model=Advertisment)
def get_advertisment(
    advertisment_id: int,
    service: AdvertismentService = Depends(),
):
    return service.get(advertisment_id=advertisment_id)


@router.put('/{advertisment_id}', response_model=Advertisment)
def update_advertisment(
    advertisment_id: int,
    advertisment_data: AdvertismentUpdate,
    service: AdvertismentService = Depends(),
):
    return service.update(
        advertisment_id=advertisment_id,
        advertisment_data=advertisment_data,
    )


@router.delete('/{advertisment_id}', response_model=Advertisment)
def delete_advertisment(
    advertisment_id: int,
    service: AdvertismentService = Depends(),
):
    service.delete(advertisment_id=advertisment_id,)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
