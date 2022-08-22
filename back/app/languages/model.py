from typing import Optional, Union

from pydantic import BaseModel

class Language(BaseModel):
    name: str
    flag: Optional[Union[str, None]] = None
