import random

import factory
from db import prisma
from users.model import Role, User, UserPost

NB_USERS = 51


class UserFactory(factory.Factory):
    class Meta:
        model = UserPost

    email = factory.Sequence(lambda n: "random{}@equidirect.com".format(n))
    firstname = factory.Faker("first_name", locale="fr_FR")
    lastname = factory.Faker("last_name", locale="fr_FR")
    password = "admin"
    role = "COMPANY"


async def create_fake_users():

    users = UserFactory.build_batch(NB_USERS)

    for user in users:
        user.role = random.SystemRandom().choice(list(Role))
        await prisma.user.create(data=user.dict())
