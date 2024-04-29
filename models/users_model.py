from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    id_api = Column(Integer, unique=True)
    nome = Column(String)
    sobrenome = Column(String)
    nomeprincipal = Column(String)
    idade = Column(Integer)
    genero = Column(String)
    telefone = Column(String)
    username = Column(String)
    password = Column(String)
    aniversario = Column(Date)



