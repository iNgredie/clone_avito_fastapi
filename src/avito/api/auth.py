from fastapi import APIRouter, Depends

from ..schemas.auth import Token, User, UserCreate
from ..services.auth import AuthService, get_current_user

router = APIRouter(
    prefix='/auth'
)


@router.post('/sign-up', response_model=Token)
def sign_up(
    user_data: UserCreate,
    service: AuthService = Depends(),
):
    return service.register_new_user(user_data)


@router.get('/user', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    return user
