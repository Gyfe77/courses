from src.api.courses import router as courses_router
from fastapi import APIRouter

main_router = APIRouter()

main_router.include_router(courses_router)