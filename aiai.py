from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
import getpass



DATABASE_URL = "mysql+mysqlconnector://root:@localhost/locadora_carros"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    ID_usuarios = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)

class Veiculo(Base):
    __tablename__ = 'veiculos'

    ID_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    placa = Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)
    valor_diaria = Column(Float, nullable=False)


def cadastrar_usuario():
    print('\n====== CADASTRO ======')
    username = input("Usuário: ")
    senha = getpass.getpass('Senha: ')

    usuario_existente = session.query(Usuario).filter_by(username = username).first()
    if usuario_existente:
        print('Esse username já está em uso. Tente outro.')
        return
    
    new_usuario = Usuario(username = username, senha = senha)
    session.add(new_usuario)
    session.commit()
    print(f'Usuario {username} cadastrado com sucesso.\n')


def login():
    print('\n====== LOGIN ======')
    username = input('Usuário: ')
    senha = getpass.getpass('Senha: ')
    usuario = session.query(Usuario).filter_by(username = username, senha = senha).first()
    if usuario:
        print(f'Bem-Vindo, {username}')
        return True
    else:
        print(f'Usuário ou senha incorreto. Tente novamente.')
        return False

def inserir(marca, modelo, placa, ano, valor_diaria):
    new_Car = Veiculo(marca=marca, modelo=modelo, placa=placa, ano=ano, valor_diaria=valor_diaria)
    session.add(new_Car)
    session.commit()
    print(f'O carro {marca} adicionado com sucesso')

def atualizar(ID_veiculo):
    car = session.query(Veiculo).filter_by(ID_veiculo = ID_veiculo).first()
    if car:
        new_placa = input("Placa: ").upper()
        new_valor_diaria = float(input("Valor da diária: "))

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
            print(f'\nID: {car.ID_veiculo}\n Marca: {car.marca}\n Modelo: {car.modelo}\n Placa: {car.placa}\n Ano: {car.ano}\n Valor da diária: {car.valor_diaria}\n ')
    else:
        print('Nenhum usuário encontrado.')

def calcular_aluguel(ID_veiculo):
    car = session.query(Veiculo).filter_by(ID_veiculo = ID_veiculo).first()
    if car:
        dias = int(input(f'Quantidade de dias que deseja alugar o carro {car.modelo}: '))
        return dias * car.valor_diaria
    
def atualizar_by_modelo(modelo):
    car = session.query(Veiculo).filter_by(modelo = modelo).first()
    if car:
        new_placa = input("Placa: ").upper()
        new_valor_diaria = float(input("Valor da diária: "))

        car.placa = new_placa
        car.valor_diaria = new_valor_diaria
        session.commit()
        print(f'Carro {modelo} atualizado.')
    else:
        print(f'Carro {modelo} não encontrado.')

def relatorio(marca):
    all_marcas = session.query(Veiculo).filter_by(marca = marca).all()
    count = len(all_marcas)
    if count > 0:
        print(f'\nExistem {count} carros da marca {marca}')
        while True:
            lista = input(f'\nListar carros encontrados? S/N\n').upper()
            if lista == 'S':
                for car in all_marcas:
                    print(f'\nID: {car.ID_veiculo}\n Marca: {car.marca}\n Modelo: {car.modelo}\n Placa: {car.placa}\n')
                break
            elif lista == 'N':
                break
            else:
                print('Comando inválido')
                continue
    else:
        print(f'Nenhum carro da marca {marca} encontrado')

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar Usuário")
        print("2. Fazer Login")
        print("3. Sair")

        choice = input("Opção: ")

        if choice == '1':
            cadastrar_usuario()
        elif choice == '2':
            if login():

                while True:
                    print("\nEscolha uma opção:")
                    print("1. Adicionar Carro")
                    print("2. Atualizar info do carro")
                    print("3. Deletar carro")
                    print("4. Listar Carros")
                    print("5. Calcular aluguel")
                    print("6. Atualizar info do carro por modelo")
                    print("7. Relatótio de carros por marca")
                    print("8. Sair")

                    choice = input("Opção: ")

                    if choice == '1':
                        marca = input("Marca do carro: ").capitalize()
                        modelo = input('Modelo: ').capitalize()
                        placa = input('Placa: ').upper()
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
                        listar()
                        ID_veiculo = int(input("ID do carro que deseja alugar: "))
                        # calcular_aluguel(ID_veiculo)
                        print(f'Valor total do aluguel: {calcular_aluguel(ID_veiculo):.2f}')
                    elif choice == '6':
                        listar()
                        modelo = input('Modelo do carro que deseja atualizar as informações: ')
                        atualizar_by_modelo(modelo)
                    elif choice == '7':
                        marca = input('Marca do relatório: ').capitalize()
                        relatorio(marca)
                    elif choice == '8':
                        print("Saindo...")
                        break
                    else:
                        print("Opção inválida. Tente novamente.")

        elif choice == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    Base.metadata.create_all(engine)  # Cria a tabela se não existir
    main()
    session.close()
