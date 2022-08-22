from db import prisma
from fastapi import HTTPException


async def check_creation_allowed(payload):
    exists_in_company = await prisma.company.find_first(where={"userId": payload.user})
    if exists_in_company:
        raise HTTPException(
            status_code=400,
            detail=f"User '{payload.user}' is already linked as Company",
        )
    exists_in_individual = await prisma.individual.find_first(
        where={"userId": payload.user}
    )
    if exists_in_individual:
        raise HTTPException(
            status_code=400,
            detail=f"User '{payload.user}' is already linked as Individual",
        )
    exists = await prisma.user.find_first(where={"id": payload.user})
    if not exists:
        raise HTTPException(
            status_code=400,
            detail=f"Can't link user with ID '{payload.user}'. Doesn't exists",
        )
