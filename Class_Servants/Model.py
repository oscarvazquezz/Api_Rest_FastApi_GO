from Connection.Connection_DB import Base
from sqlalchemy.sql.sqltypes import Integer,String,Boolean
from sqlalchemy import  Column,ForeignKey
from sqlalchemy.orm import relationship

class Class_Servant(Base):
    __tablename__ = "Class_Servants"
    id= Column(Integer,primary_key=True,index=True)
    name_Class = Column(String)
    Servants = relationship("Servant", back_populates="owner")