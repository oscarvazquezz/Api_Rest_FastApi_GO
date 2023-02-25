from pydantic import BaseModel, Field
from typing import Optional
from typing import List, Union

class Servants(BaseModel):
    __tablename__ = "Servants"
    name_Servant : str
    skill_One : str
    skill_Two : str
    skill_Three : str
    noble_Phantasm : str
    type_Noble_phantasm : str

class schema_Servants(Servants):
    pass
