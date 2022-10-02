from typing import List, Optional, Union

from db import prisma
from entities.users.model import UserRead, UserUpdate
from fastapi import HTTPException
from routers.users import router
from utils import dict_tools


@router.get("/", tags=["users"], response_model=Union[List[UserRead], UserRead, None])
async def get_users(
    email: Optional[str] = None,
    lastname: Optional[str] = None,
    firstname: Optional[str] = None,
    role: Optional[str] = None,
    confirmation_id: Optional[str] = None,
    confirmed: Optional[bool] = None,
    last_email_send: Optional[int] = None,
    multiple: bool = True,
) -> UserRead | List[UserRead]:

    filters = {}
    if email:
        filters["email"] = email
    if lastname:
        filters["lastname"] = lastname
    if firstname:
        filters["firstname"] = firstname
    if role:
        filters["role"] = role
    if confirmation_id:
        filters["confirmation_id"] = confirmation_id
    if confirmed:
        filters["confirmed"] = confirmed
    if last_email_send:
        filters["last_email_send"] = last_email_send

    if not multiple:
        user = await prisma.user.find_first(where=filters)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found",
            )
        return user
    else:
        return await prisma.user.find_many(where=filters)


@router.put("/{user_id}", tags=["users"], response_model=UserRead)
async def update_user(user_id: int, user_in: UserUpdate) -> UserRead:
    user = user_in.dict()
    dict_tools.cleanEmptyValue(user, list(user.items()))
    updated = await prisma.user.update(
        where={"id": user_id},
        data=user,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail=f"Can't update user with ID '{user_id}' which doesn't exists",
        )

    return updated


@router.delete("/{user_id}", tags=["users"], response_model=UserRead)
async def delete_user(user_id: int) -> UserRead:
    deleted = await prisma.user.delete(where={"id": user_id})

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail=f"Can't delete user with ID '{user_id}' which doesn't exists",
        )

    return deleted
