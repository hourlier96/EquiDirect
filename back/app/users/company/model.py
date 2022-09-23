from typing import Optional, Union

from users.model import UserCommonInformation


class Company(UserCommonInformation):
    housingProvider: Optional[Union[bool, None]] = None
    workProvider: Optional[Union[bool, None]] = None


class CompanyIn(Company):
    user: int  # Foreign key
    language: Optional[Union[int, None]] = None  # Foreign key
