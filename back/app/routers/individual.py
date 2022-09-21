from fastapi import APIRouter, Depends

from auth.jwt import JWTBearer

router = APIRouter(
    prefix="/individual",
    tags=["individuals"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(JWTBearer())],
)
