from fastapi import APIRouter

router = APIRouter(
    prefix="/individual",
    tags=["individuals"],
    responses={404: {"description": "Not found"}},
)
