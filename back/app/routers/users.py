from fastapi import APIRouter, Depends

from auth.jwt import JWTBearer

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(JWTBearer())],
)
