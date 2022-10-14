from typing import List, Optional, Union

from db import prisma
from entities.users.individual.model import Individual
from fastapi import HTTPException
from routers.individual import router


@router.get(
    "/", tags=["individuals"], response_model=Union[List[Individual], Individual, None]
)
async def get_individual(
    user_id: Optional[int] = None,
    multiple: bool = True,
) -> List[Individual]:

    filters = {}
    if user_id:
        filters["userId"] = user_id

    if not multiple:
        individual = await prisma.individual.find_first(where=filters)
        if not individual:
            raise HTTPException(
                status_code=404,
                detail="Individual not found",
            )
        return individual
    else:
        return await prisma.individual.find_many(where=filters)


@router.put("/{individual_id}", tags=["individuals"], response_model=Individual)
async def update_invididual(individual_id: int, individual_in: Individual):

    exists = await prisma.individual.find_first(where={"id": individual_id})
    if not exists:
        raise HTTPException(
            status_code=400,
            detail=f"Can't update individual with ID '{individual_id}' which doesn't exists",
        )

    payload = individual_in.dict()
    updated = await prisma.individual.update(where={"id": individual_id}, data=payload)
    return updated


@router.delete("/{individual_id}", tags=["individuals"], response_model=Individual)
async def delete_invididual(individual_id: int):

    exists = await prisma.individual.find_first(where={"id": individual_id})
    if not exists:
        raise HTTPException(
            status_code=400,
            detail=f"Can't delete individual with ID '{individual_id}' which doesn't exists",
        )

    deleted = await prisma.individual.delete(where={"id": individual_id})
    return deleted
