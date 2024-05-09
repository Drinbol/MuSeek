from fastapi import APIRouter
from .root_api import router as root_router

router = APIRouter()
router.include_router(root_router, tags=["Root"])
