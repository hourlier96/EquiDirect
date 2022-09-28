from fastapi import APIRouter

router = APIRouter(
    prefix="/email",
    tags=["email"],
    responses={404: {"description": "Not found"}},
)
