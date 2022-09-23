from db import prisma
from entities.users.controller import get_users
from entities.users.model import User, UserPost
from fastapi import HTTPException, status
from routers.auth import router
from utils.hash import check_password, hash_password, new_salt

from auth.jwt import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from auth.model import Token, UserLogin


async def authenticate_user(user_login: UserLogin):
    user = await get_users(email=user_login.email)
    if not user:
        return False
    if not check_password(user_login.password, user.password):
        return False
    return user


@router.post("/token", response_model=Token)
async def access_token(user_login: UserLogin):
    user = await authenticate_user(user_login)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        user={
            "sub": user.email,
            "firstname": user.firstname,
            "lastname": user.lastname,
            "role": user.role,
        },
        expires_delta=ACCESS_TOKEN_EXPIRE_MINUTES,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", response_model=User)
async def create_user(user_in: UserPost) -> User:
    exists = await prisma.user.find_first(where={"email": user_in.email})
    if exists:
        raise HTTPException(status_code=400, detail="Email already taken")
    salt = new_salt()
    user_in.salt = salt.decode("utf-8")
    user_in.password = hash_password(user_in.password.encode("utf-8"), salt)
    created = await prisma.user.create(data=user_in.dict())
    return created
