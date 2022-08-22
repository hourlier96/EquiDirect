import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from db import prisma
from users.company.controller import router as router_company
from users.controller import router as router_users
from users.individual.controller import router as router_individual

load_dotenv()

app = FastAPI()
app.include_router(router_users, prefix=os.getenv("API_PREFIX"))
app.include_router(router_individual, prefix=os.getenv("API_PREFIX"))
app.include_router(router_company, prefix=os.getenv("API_PREFIX"))


@app.on_event("startup")
async def startup() -> None:
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await prisma.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, debug=True)
