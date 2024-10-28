from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqlconnector://root:@localhost/locadora_carros"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Locadora(Base):
    __tablename__ = 'Locadora'

    ID_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    placa = Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)
    valor_diaria = Column(Integer, nullable=False)

def inserir(marca, modelo, placa, ano, valor_Diaria):
    new_Car = Locadora(marca=marca, modelo=modelo, placa=placa, ano=ano, valor_Diaria=valor_Diaria)
    session.add(Locadora)
    session.commit()
    print(f'O carro {marca} adicionado com sucesso')

'''ID_veiculo (INT, PRIMARY KEY, AUTO_INCREMENT): Identificador único do veículo.
marca (VARCHAR): Marca do veículo.
modelo (VARCHAR): Modelo do veículo.
placa (VARCHAR): Placa do veículo.
ano (INT): Ano de fabricação do veículo.
valor_diaria (DECIMAL): Valor da diária do veículo.'''