import random
import string

import factory
from db import prisma
from users.model import Role, User, UserPost
from utils.hash import hash_password, new_salt

NB_USERS = 51


class UserFactory(factory.Factory):
    class Meta:
        model = UserPost

    email = factory.Sequence(lambda n: "random{}@equidirect.com".format(n))
    firstname = factory.Faker("first_name", locale="fr_FR")
    lastname = factory.Faker("last_name", locale="fr_FR")
    salt = new_salt()
    password = hash_password(
        "password".encode("utf-8"),
        salt,
    )
    role = "COMPANY"


async def create_fake_users():

    users = UserFactory.build_batch(NB_USERS)

    for user in users:
        user.role = random.SystemRandom().choice(list(Role))
        salt = new_salt()
        user.salt = salt.decode("utf-8")
        user.password = hash_password(
            "password".encode("utf-8"),
            salt,
        )
        await prisma.user.create(data=user.dict())
