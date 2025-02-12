from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cart(Base):
    __tablename__ = 'cart'

    id_api = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    products = Column(String)
