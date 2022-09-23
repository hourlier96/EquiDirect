from typing import List, Optional, Union

from db import prisma
from entities.users.model import User
from fastapi import HTTPException
from routers.users import router


@router.get("/", tags=["users"], response_model=Union[List[User], User, None])
async def get_users(email: Optional[str] = None) -> User | List[User]:
    if email:
        return await prisma.user.find_unique(where={"email": email})

    return await prisma.user.find_many()


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
