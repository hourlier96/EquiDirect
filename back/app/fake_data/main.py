import asyncio

from db import prisma
from dotenv import load_dotenv

from .company_factory import create_fake_companys
from .individual_factory import create_fake_individuals
from .language_factory import create_fake_languages
from .user_factory import create_fake_users


async def on_startup():
    load_dotenv()

    await prisma.connect()
    await prisma.execute_raw(
        query="""
        TRUNCATE TABLE \"Language\" RESTART IDENTITY CASCADE;
        """
    )
    await prisma.execute_raw(
        query="""
        TRUNCATE TABLE \"User\" RESTART IDENTITY CASCADE;
        """
    )


async def on_shutdown():
    await prisma.disconnect()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(on_startup())
    loop.run_until_complete(create_fake_users())
    loop.run_until_complete(create_fake_languages())
    loop.run_until_complete(create_fake_individuals())
    loop.run_until_complete(create_fake_companys())
    loop.run_until_complete(on_shutdown())
    loop.close()
