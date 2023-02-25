from pydantic import BaseModel, Field
from typing import Optional
from typing import List, Union

class schema_Class_Servant(BaseModel):
    __tablename__ = "Class_Servants"
    name_Class:str

class schema_Class_Servants(BaseModel):
    __tablename__ = "Class_Servant"
    id:int
