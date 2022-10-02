from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Field


class Role(str, Enum):
    INDIVIDUAL = "INDIVIDUAL"
    COMPANY = "COMPANY"


class UserPost(BaseModel):
    email: str
    lastname: str
    firstname: str
    password: str
    role: Role
    confirmation_id: Optional[str]  # For faker
    confirmed: Optional[bool]  # For faker
    last_email_send: Optional[datetime] = Field(None)

    class Config:
        use_enum_values = True


class UserRead(UserPost):
    id: int
    confirmation_id: str
    confirmed: bool
    last_email_send: Optional[datetime] = Field(None)

    class Config:
        use_enum_values = True


class UserUpdate(BaseModel):
    email: Optional[str] = None
    lastname: Optional[str] = None
    firstname: Optional[str] = None
    role: Optional[Role] = None
    confirmed: Optional[bool] = None
    last_email_send: Optional[datetime] = None

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
