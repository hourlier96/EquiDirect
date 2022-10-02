import datetime
import random

import factory
from db import prisma
from entities.users.model import Role, UserPost
from utils.hash import hash_password, new_salt
from utils.randomizer import get_random_uuid

NB_USERS = 51


class UserFactory(factory.Factory):
    class Meta:
        model = UserPost

    email = factory.Sequence(lambda n: "random{}@equisphere.com".format(n))
    firstname = factory.Faker("first_name", locale="fr_FR")
    lastname = factory.Faker("last_name", locale="fr_FR")
    salt = new_salt()
    password = hash_password(
        "password".encode("utf-8"),
        salt,
    )
    role = "COMPANY"
    confirmation_id = get_random_uuid()
    confirmed = False
    last_email_send = None


async def create_fake_users():

    users = UserFactory.build_batch(NB_USERS)

    for user in users:
        user.role = random.SystemRandom().choice(list(Role))
        salt = new_salt()
        user.password = hash_password(
            "password".encode("utf-8"),
            salt,
        )
        user.confirmation_id = get_random_uuid()
        user.last_email_send = None
        await prisma.user.create(data=user.dict())
