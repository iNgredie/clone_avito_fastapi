from fastapi import APIRouter

from .advertisment import router as advertisment_router
from .auth import router as auth_router
from .category import router as category_router

router = APIRouter()
router.include_router(advertisment_router)
router.include_router(auth_router)
router.include_router(category_router)
