import factory
from db import prisma
from languages.model import Language

NB_LANGUAGES = 100


class LanguageFactory(factory.Factory):
    class Meta:
        model = Language

    name = factory.Faker("language_name")
    flag = None


async def create_fake_languages():

    languages = LanguageFactory.build_batch(NB_LANGUAGES)

    for language in languages:
        exists = await prisma.language.find_first(where={
            "name": language.name
        })
        while exists:
            language.name = LanguageFactory().name
            exists = await prisma.language.find_first(where={
                "name": language.name
            })
        await prisma.language.create(data=language.dict())
