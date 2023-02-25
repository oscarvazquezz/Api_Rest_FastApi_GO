from Connection.Connection_DB import Base
from sqlalchemy.sql.sqltypes import Integer,String,Boolean
from sqlalchemy import  Column,ForeignKey
from sqlalchemy.orm import relationship
from Class_Servants.Model import Class_Servant

class Servant(Base):
    __tablename__ = "Servants"

    id_Servant= Column(Integer,primary_key=True, index=True)
    name_Servant = Column(String)
    skill_One = Column(String)
    skill_Two = Column(String)
    skill_Three = Column(String)
    noble_Phantasm = Column(String)
    type_Noble_phantasm = Column(String)
    owner_id = Column(Integer,ForeignKey("Class_Servants.id"))
    owner = relationship("Class_Servant", back_populates="Servants")