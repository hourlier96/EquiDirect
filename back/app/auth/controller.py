import json

from db import prisma
from entities.users.company.model import Company, CompanyIn
from entities.users.controller import delete_user, get_users
from entities.users.individual.model import Individual, IndividualIn
from entities.users.model import UserPost, UserReadRegistration
from fastapi import HTTPException, status
from routers.auth import router
from utils.controller_checks import check_creation_allowed
from utils.hash import check_password, hash_password, new_salt
from utils.prisma_connect import set_foreign_key
from utils.randomizer import get_random_uuid

from auth.jwt import ACCESS_TOKEN_EXPIRE, create_access_token
from auth.model import Token, UserLogin


async def authenticate_user(user_login: UserLogin):
    user = await get_users(email=user_login.email, multiple=False)
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
        expires_delta=ACCESS_TOKEN_EXPIRE,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", response_model=UserReadRegistration)
async def create_user(user_in: UserPost) -> UserReadRegistration:
    exists = await prisma.user.find_first(where={"email": user_in.email})
    if exists:
        raise HTTPException(status_code=400, detail="Email already taken")
    salt = new_salt()
    user_in.password = hash_password(user_in.password.encode("utf-8"), salt)
    user_in.confirmation_id = get_random_uuid()
    user_in.confirmed = False
    user_in.last_email_send = None
    try:
        created = await prisma.user.create(data=user_in.dict())
        if user_in.role == "COMPANY":
            await create_company(CompanyIn.parse_obj({"user": created.id}))
        if user_in.role == "INDIVIDUAL":
            await create_individual(IndividualIn.parse_obj({"user": created.id}))
    except Exception:
        if created:
            await delete_user(created.id)
        raise HTTPException(
            status_code=500,
            detail="An error happened during registration, please try later",
        )
    return created


@router.post("/", tags=["individuals"], response_model=Individual)
async def create_individual(individual_in: IndividualIn):

    await check_creation_allowed(individual_in)

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


@router.post("/", tags=["companys"], response_model=Company)
async def create_company(company_in: CompanyIn):

    check_creation_allowed(company_in)

    data = company_in.dict()
    set_foreign_key(data, "user", company_in.user)
    if "language" in data:
        set_foreign_key(data, "language", company_in.language)

    created = await prisma.company.create(data=data)
    return created
