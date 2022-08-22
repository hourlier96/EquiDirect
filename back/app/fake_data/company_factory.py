import json
import random

import factory
from db import prisma
from users.model import Company, Discipline, Skills, WorkTime, WorkType
from utils.prisma_connect import set_foreign_key

NB_COMPANY = 25


class CompanyFactory(factory.Factory):
    class Meta:
        model = Company

    userId = 0
    languageId = random.randint(1, 1)
    address = factory.Faker("address", locale="fr_FR")
    disciplines = [random.SystemRandom().choice(list(Discipline))]
    housingProvider = bool(random.getrandbits(1))
    workProvider = bool(random.getrandbits(1))
    # profilPicture
    # professionnalCard
    # license
    rate = round(random.uniform(0, 5.0), 2)


async def create_fake_companys():

    companys = CompanyFactory.build_batch(NB_COMPANY)

    for company in companys:

        company.disciplines = [random.SystemRandom().choice(list(Discipline))]
        company.housingProvider = bool(random.getrandbits(1))
        company.workProvider = bool(random.getrandbits(1))
        # profilPicture
        # professionnalCard
        # license
        company.rate = round(random.uniform(0, 5.0), 2)
        data = company.dict()
        CompanyFactory.userId = CompanyFactory.userId + 2
        set_foreign_key(data, "user", CompanyFactory.userId)
        set_foreign_key(data, "language", 1)
        await prisma.company.create(data=data)
