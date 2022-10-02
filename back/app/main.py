import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.controller import router as router_auth
from db import prisma
from entities.users.company.controller import router as router_company
from entities.users.controller import router as router_users
from entities.users.individual.controller import router as router_individual
from mail.controller import router as router_mail

load_dotenv()

app = FastAPI()

app.include_router(router_auth, prefix=os.getenv("API_PREFIX"))
app.include_router(router_users, prefix=os.getenv("API_PREFIX"))
app.include_router(router_individual, prefix=os.getenv("API_PREFIX"))
app.include_router(router_company, prefix=os.getenv("API_PREFIX"))
app.include_router(router_mail, prefix=os.getenv("API_PREFIX"))

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup() -> None:
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await prisma.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, debug=True)
