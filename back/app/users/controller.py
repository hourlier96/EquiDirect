from typing import List

from db import prisma
from fastapi import HTTPException
from routers.users import router

from users.model import User


@router.get("/", tags=["users"], response_model=List[User])
async def get_users() -> List[User]:
    users = await prisma.user.find_many()
    return users


@router.post("/", tags=["users"], response_model=User)
async def create_user(user_in: User) -> User:
    exists = await prisma.user.find_first(where={"email": user_in.email})
    if exists:
        raise HTTPException(status_code=400, detail="Email already taken")

    created = await prisma.user.create(data=user_in.dict())

    return created


@router.put("/{user_id}", tags=["users"], response_model=User)
async def update_user(user_id: int, user_in: User) -> User:
    updated = await prisma.user.update(
        where={
            "id": user_id,
        },
        data=user_in.dict(),
    )

    if not updated:
        raise HTTPException(
            status_code=400,
            detail=f"Can't update user with ID '{user_id}' which doesn't exists",
        )

    return updated


@router.delete("/{user_id}", tags=["users"], response_model=User)
async def delete_user(user_id: int) -> User:
    deleted = await prisma.user.delete(where={"id": user_id})

    if not deleted:
        raise HTTPException(
            status_code=400,
            detail=f"Can't delete user with ID '{user_id}' which doesn't exists",
        )

    return deleted
