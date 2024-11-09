from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Produtos(Base):
    __tablename__ = 'produtos'

    ID_produto = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(50), nullable=False)
    cor = Column(String(50), nullable=False)
    estoque = Column(Integer, nullable=False)
    valor = Column(Float, nullable=False)
