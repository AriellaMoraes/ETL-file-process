from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True)
    id_api = Column(Integer, unique=True)
    titulo = Column(String)
    descricao = Column(String)
    preco = Column(Float)
    desconto = Column(Float)
    nota = Column(Float)
    estoque = Column(Integer)
    marca = Column(String)
    categoria = Column(String)