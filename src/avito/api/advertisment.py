from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.openapi.models import Response

from ..schemas.advertisment import (
    Advertisment, AdvertismentCreate, AdvertismentUpdate
)
from ..schemas.auth import User
from ..services.advertisment import AdvertismentService
from ..services.auth import get_current_user

router = APIRouter(
    prefix='/advertisment',
    tags=['advertisment'],
)


@router.get('/', response_model=List[Advertisment])
def get_advertisments(
    user: User = Depends(get_current_user),
    service: AdvertismentService = Depends(),
):
    return service.get_list(user_id=user.id)


@router.post('/', response_model=Advertisment)
def create_advertisment(
    advertisment_data: AdvertismentCreate,
    user: User = Depends(get_current_user),
    service: AdvertismentService = Depends(),
):
    return service.create(user_id=user.id, advertisment_data=advertisment_data)


@router.get('/{advertisment_id}', response_model=Advertisment)
def get_advertisment(
    advertisment_id: int,
    user: User = Depends(get_current_user),
    service: AdvertismentService = Depends(),
):
    return service.get(user_id=user.id, advertisment_id=advertisment_id)


@router.put('/{advertisment_id}', response_model=Advertisment)
def update_advertisment(
    advertisment_id: int,
    advertisment_data: AdvertismentUpdate,
    user: User = Depends(get_current_user),
    service: AdvertismentService = Depends(),
):
    return service.update(
        user_id=user.id,
        advertisment_id=advertisment_id,
        advertisment_data=advertisment_data,
    )


@router.delete('/{advertisment_id}', response_model=Advertisment)
def delete_advertisment(
    advertisment_id: int,
    user: User = Depends(get_current_user),
    service: AdvertismentService = Depends(),
):
    service.delete(user_id=user.id, advertisment_id=advertisment_id,)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
