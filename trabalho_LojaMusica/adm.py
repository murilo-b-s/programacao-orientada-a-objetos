from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Adm(Base):
    __tablename__ = 'Administrador'

    ID_produto = Column(Integer, primary_key=True, autoincrement=True)
    admin = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)