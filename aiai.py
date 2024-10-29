from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqlconnector://root:@localhost/locadora_carros"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Veiculo(Base):
    __tablename__ = 'veiculos'

    ID_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    placa = Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)
    valor_diaria = Column(Float, nullable=False)

def inserir(marca, modelo, placa, ano, valor_diaria):
    new_Car = Veiculo(marca=marca, modelo=modelo, placa=placa, ano=ano, valor_diaria=valor_diaria)
    session.add(new_Car)
    session.commit()
    print(f'O carro {marca} adicionado com sucesso')

def atualizar(ID_veiculo):
    car = session.query(Veiculo).filter_by(ID_veiculo = ID_veiculo).first()
    if car:
        new_placa = input("Placa: ")
        new_valor_diaria = input("Valor da diária: ")

        car.placa = new_placa
        car.valor_diaria = new_valor_diaria
        session.commit()
        print(f'Carro {id} atualizado.')
    else:
        print(f'Carro {id} não encontrado.')

def excluir(ID_veiculo):
    car = session.query(Veiculo).filter_by(ID_veiculo = ID_veiculo).first()
    modelo_car = car.modelo
    if car:
        session.delete(car)
        session.commit()
        print(f'Carro {id}{modelo_car} excluido.')
    else:
        print(f'Carro {id} não encontrado.')

def listar():
    all_cars = session.query(Veiculo).all()
    if all_cars:
        for car in all_cars:
            print(f'ID: {car.ID_veiculo}\n Modelo: {car.modelo}\n Placa: {car.placa}\n Ano: {car.ano}\n Valor da diária: {car.valor_diaria} ')
    else:
        print('Nenhum usuário encontrado.')



def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar Carro")
        print("2. Atualizar info do carro")
        print("3. Deletar carro")
        print("4. Listar Carros")
        print("5. Sair")

        choice = input("Opção: ")

        if choice == '1':
            marca = input("Marca do carro: ")
            modelo = input('Modelo:')
            placa = input('Placa:')
            ano = int(input("Ano: "))
            valor_diaria = float(input("Valor da diária: "))
            inserir(marca, modelo, placa, ano, valor_diaria)
        elif choice == '2':
            listar()
            ID_veiculo = int(input("ID do carro a ser atualizado: "))
            atualizar(ID_veiculo)
        elif choice == '3':
            listar()
            ID_veiculo = int(input("ID do carro a ser atualizado: "))
            excluir(ID_veiculo)
        elif choice == '4':
            listar()
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    Base.metadata.create_all(engine)  # Cria a tabela se não existir
    main()
    session.close()


'''ID_veiculo (INT, PRIMARY KEY, AUTO_INCREMENT): Identificador único do veículo.
marca (VARCHAR): Marca do veículo.
modelo (VARCHAR): Modelo do veículo.
placa (VARCHAR): Placa do veículo.
ano (INT): Ano de fabricação do veículo.
valor_diaria (DECIMAL): Valor da diária do veículo.'''