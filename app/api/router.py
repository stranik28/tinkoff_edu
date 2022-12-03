from fastapi import APIRouter, Depends
from app.services.test import get_test_adapter


router = APIRouter(prefix="/test", tags=["test"])

@router.get("/")
async def test(test_adapter=Depends(get_test_adapter)):
    return test_adapter.get_all()
