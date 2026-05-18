from __future__ import annotations
from sqlalchemy import DateTime,ForeignKey,String,Text,Integer
from sqlalchemy.orm import Mapped,mapped_column,relationship
from .database import Base

class Student(Base):
    __tablename__= "students"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    name:Mapped[str]=mapped_column(String(50),unique=True,nullable=False)
    
