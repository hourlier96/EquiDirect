import json
from enum import Enum
from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class Role(str, Enum):
    INDIVIDUAL = "INDIVIDUAL"
    COMPANY = "COMPANY"


class User(BaseModel):
    email: str
    lastname: Union[str, None] = None
    firstname: Union[str, None] = None
    role: Role

    class Config:
        use_enum_values = True


# COMMON INFORMATIONS


class Discipline(str, Enum):
    CSO = "CSO"
    CCE = "CCE"
    Dressage = "Dressage"
    Voltige = "Voltige"
    Equifeel = "Equifeel"
    Hunter = "Hunter"
    Western = "Western"
    PonyGames = "PonyGames"
    EquiFun = "EquiFun"
    Attelage = "Attelage"
    Endurance = "Endurance"
    HorseBall = "HorseBall"
    Polo = "Polo"


class UserCommonInformation(BaseModel):
    address: Optional[Union[str, None]] = None
    disciplines: List[Discipline] = []
    profilPicture: Optional[Union[str, None]] = None
    rate: Optional[Union[float, None]] = None


# INDIVIDUAL


class Skills(str, Enum):
    Conduite_de_tracteur = "Conduite_de_tracteur"
    Travail_a_pied = "Travail_a_pied"
    Travail_Monte = "Travail_Monte"
    Autonomie = "Autonomie"
    Gestion_de_cheptel = "Gestion_de_cheptel"
    Manipulation_entier = "Manipulation_entier"
    Debourrage = "Debourrage"
    Toilettage = "Toilettage"
    Premiers_soins = "Premiers_soins"
    Petits_bricolages = "Petits_bricolages"
    Animation = "Animation"
    Tourisme_equestre = "Tourisme_equestre"
    EquiHandi = "EquiHandi"
    Baby_Poney = "Baby_Poney"
    Coaching_en_competition = "Coaching_en_competition"
    Sortie_en_concours_AM_PRO = "Sortie_en_concours_AM_PRO"


class WorkType(str, Enum):
    WorkType = "WorkType1"


class WorkTime(str, Enum):
    Punctual = "Ponctuel"
    Indefinite = "Indefini"


class Individual(UserCommonInformation):

    skills: List[Skills] = []
    galop: Optional[Union[int, None]] = None
    maxMoveKm: Optional[Union[int, None]] = None
    selfEmployed: Optional[Union[bool, None]] = None
    searchingWork: Optional[Union[bool, None]] = None
    workType: List[WorkType] = []
    workTime: Optional[Union[str, None]] = None
    experience: Optional[Union[int, None]] = None
    prices: Optional[Union[Dict, None]] = None
    housingNeed: Optional[Union[bool, None]] = None
    profilPicture: Optional[Union[str, None]] = None
    professionnalCard: Optional[Union[str, None]] = None
    license: Optional[Union[str, None]] = None
    rate: Optional[Union[float, None]] = None

    class Config:
        use_enum_values = True


class IndividualIn(Individual):
    user: int  # Foreign key
    language: Optional[Union[int, None]] = None  # Foreign key


# COMPANY


class Company(UserCommonInformation):
    housingProvider: Optional[Union[bool, None]] = None
    workProvider: Optional[Union[bool, None]] = None


class CompanyIn(Company):
    user: int  # Foreign key
    language: Optional[Union[int, None]] = None  # Foreign key
