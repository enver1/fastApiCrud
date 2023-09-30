from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import Base

class Usuario(Base):
    __tablename__ = 'users'
    codigo = Column(Integer, primary_key=True)
    nombre = Column(String(255))              

