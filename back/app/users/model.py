from enum import Enum
from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class Role(str, Enum):
    INDIVIDUAL = "INDIVIDUAL"
    COMPANY = "COMPANY"


class User(BaseModel):
    email: str
    salt: str = None
    lastname: Union[str, None] = None
    firstname: Union[str, None] = None
    role: Role

    class Config:
        use_enum_values = True


class UserPost(User):
    password: str


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
