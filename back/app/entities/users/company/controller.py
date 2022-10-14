from typing import List

from db import prisma
from entities.users.company.model import Company
from fastapi import HTTPException
from routers.company import router


@router.get("/", tags=["companys"], response_model=List[Company])
async def get_company() -> List[Company]:

    companys = await prisma.company.find_many()
    return companys


@router.put("/{company_id}", tags=["companys"], response_model=Company)
async def update_company(company_id: int, company_in: Company):

    exists = await prisma.company.find_first(where={"id": company_id})
    if not exists:
        raise HTTPException(
            status_code=400,
            detail=f"Can't update individual with ID '{company_id}' which doesn't exists",
        )

    payload = company_in.dict()
    updated = await prisma.company.update(where={"id": company_id}, data=payload)
    return updated


@router.delete("/{company_id}", tags=["companys"], response_model=Company)
async def delete_company(company_id: int):

    exists = await prisma.company.find_first(where={"id": company_id})
    if not exists:
        raise HTTPException(
            status_code=400,
            detail=f"Can't delete company with ID '{company_id}' which doesn't exists",
        )

    deleted = await prisma.individual.delete(where={"id": company_id})
    return deleted
