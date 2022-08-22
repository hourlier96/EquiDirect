import json
from typing import List, Union

from db import prisma
from fastapi import HTTPException
from routers.individual import router
from users.model import Individual, IndividualIn
from utils.controller_checks import check_creation_allowed
from utils.prisma_connect import set_foreign_key


@router.get("/", tags=["individuals"], response_model=List[Individual])
async def get_individual() -> List[Individual]:
    individuals = await prisma.individual.find_many()
    return individuals


@router.post("/", tags=["individuals"], response_model=Individual)
async def create_individual(individual_in: IndividualIn):

    check_creation_allowed(individual_in)

    data = individual_in.dict()
    set_foreign_key(data, "user", individual_in.user)
    if data["language"] is None:
        del data["language"]
    else:
        set_foreign_key(data, "language", individual_in.language)
    if "prices" in data:
        data["prices"] = json.dumps(data["prices"])

    created = await prisma.individual.create(data=data)
    return created


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
