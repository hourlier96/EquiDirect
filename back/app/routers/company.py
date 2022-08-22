from fastapi import APIRouter

router = APIRouter(
    prefix="/companys",
    tags=["companys"],
    responses={404: {"description": "Not found"}},
)
