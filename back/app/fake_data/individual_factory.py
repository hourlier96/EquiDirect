import json
import random

import factory
from db import prisma
from entities.users.individual.model import Individual, Skills, WorkTime, WorkType
from entities.users.model import Discipline
from utils.prisma_connect import set_foreign_key

NB_INDIVIDUAL = 25


class IndividualFactory(factory.Factory):
    class Meta:
        model = Individual

    userId = -1
    languageId = random.randint(1, 1)
    address = factory.Faker("address", locale="fr_FR")
    disciplines = [random.SystemRandom().choice(list(Discipline))]
    skills = [random.SystemRandom().choice(list(Skills))]
    galop = random.randint(1, 7)
    maxMoveKm = random.randint(1, 200)
    selfEmployed = bool(random.getrandbits(1))
    searchingWork = bool(random.getrandbits(1))
    workTime = random.SystemRandom().choice(list(WorkTime))
    experience = random.randint(1, 20)
    prices = {
        "max": random.randint(1800, 2500),
        "min": random.randint(800, 1200),
        "travel_price": random.randint(5, 40),
    }
    housingNeed = bool(random.getrandbits(1))
    # profilPicture
    # professionnalCard
    # license
    rate = round(random.uniform(0, 5.0), 2)


async def create_fake_individuals():

    individuals = IndividualFactory.build_batch(NB_INDIVIDUAL)

    for individual in individuals:
        individual.disciplines = [random.SystemRandom().choice(list(Discipline))]
        individual.skills = [random.SystemRandom().choice(list(Skills))]
        individual.galop = random.randint(1, 7)
        individual.maxMoveKm = random.randint(1, 200)
        individual.selfEmployed = bool(random.getrandbits(1))
        individual.searchingWork = bool(random.getrandbits(1))
        individual.workType = [random.SystemRandom().choice(list(WorkType))]
        individual.workTime = random.SystemRandom().choice(list(WorkTime))
        individual.experience = random.randint(1, 20)
        individual.prices = json.dumps(
            {
                "max": random.randint(1800, 2500),
                "min": random.randint(800, 1200),
                "travel_price": random.randint(5, 40),
            }
        )
        individual.housingNeed = bool(random.getrandbits(1))
        # profilPicture
        # professionnalCard
        # license
        individual.rate = round(random.uniform(0, 5.0), 2)
        data = individual.dict()
        IndividualFactory.userId = IndividualFactory.userId + 2
        set_foreign_key(data, "user", IndividualFactory.userId)
        set_foreign_key(data, "language", 1)
        await prisma.individual.create(data=data)
