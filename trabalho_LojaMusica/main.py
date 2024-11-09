from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
import getpass
from usuario import Usuario
from produtos import Produtos
from adm import Adm


DATABASE_URL = "mysql+mysqlconnector://root:@localhost/lojamusica"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Adm(Base):
    __tablename__ = 'Administrador'

    ID_produto = Column(Integer, primary_key=True, autoincrement=True)
    admin = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)


def cadastrar_usuario():
    print('='*10+' CADASTRO '+'='*10)
    username = input("Username: ")
    senha = getpass.getpass('Senha:')

    username_existente = session.query(Usuario).filter_by(username = username).first()
    if username_existente:
        print(f'O username {username} já está ativo. Tente outro.')
        return

    new_usuario = Usuario(username = username, senha = senha)
    session.add(new_usuario)
    session.commit()
    print(f'Usuario {username} cadastrado com sucesso.\n')

def login():
    print('='*10+' LOGIN '+'='*10)
    username = input("Username: ")
    senha = getpass.getpass('Senha:')

    usuario = session.query(Usuario).filter_by(username = username, senha = senha).first()
    if usuario:
        print(f'Bem-Vindo, {username}')
        return True
    else:
        print(f'Usuário ou senha incorreto. Tente novamente.')
        return False

def criar_admin_padrao():
    admin_existente = session.query(Adm).filter_by(admin='administrador').first()
    if not admin_existente:
        adm = Adm(admin='administrador', senha='1234')
        session.add(adm)
        session.commit()
        print('Administrador padrão criado.')

def login_admin():
    print('='*10+' LOGIN ADMIN '+'='*10)
    admin = input("Username: ")
    senha = getpass.getpass('Senha:')

    usuario = session.query(Adm).filter_by(admin = admin, senha = senha).first()
    if usuario:
        print(f'Bem-Vindo, {admin}')
        return True
    print(f'Usuário ou senha incorreto. Tente novamente.')
    return False

def cadastro_produto():
    categoria = input('Categoria: ')
    cor = input('Cor: ')
    estoque = int(input('Quantidade no estoque: '))
    valor = float(input('Valor: '))

    produto_existente = session.query(Produtos).filter_by(categoria = categoria, cor = cor).first()
    if produto_existente:
        print('Já existe peças identicas a essa no estoque. Se quiser atualizar escolha outra opção.')
        return
    
    new_produto = Produtos(categoria = categoria, cor = cor, estoque = estoque, valor = valor)
    session.add(new_produto)
    session.commit()
    print(f'O produto {categoria} de cor {cor} foi adicionado com sucesso!')


if __name__ == "__main__":
    
    Base.metadata.create_all(engine)  # Cria a tabela se não existir
    criar_admin_padrao()
    # login_admin()
    # cadastro_produto()
    while True:
        print("\n--- Menu Principal ---")
        print("1. Login Usuário")
        print("2. Cadastrar Usuário")
        print("3. Login Administrador")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            if login():  # Realiza o login do usuário
                print("\n--- Menu do Usuário ---")
                usuario = session.query(Usuario).filter_by(username=input("Digite seu username: ")).first()
                while True:
                    print("\n1. Comprar Produto")
                    print("2. Logout")
                    opcao_usuario = input("Escolha uma opção: ")

                    if opcao_usuario == '1':
                        usuario.comprar()  # Chama a função `comprar` do usuário logado
                    elif opcao_usuario == '2':
                        print("Logout realizado.")
                        break
                    else:
                        print("Opção inválida.")

        elif opcao == '2':
            cadastrar_usuario()  # Chama a função para cadastrar um novo usuário

        elif opcao == '3':
            if login_admin():  # Realiza o login do administrador
                print("Bem-vindo, Administrador.")
                while True:
                    print("\n--- Menu do Administrador ---")
                    print("1. Cadastrar Produto")
                    print("2. Logout")
                    opcao_admin = input("Escolha uma opção: ")

                    if opcao_admin == '1':
                        cadastro_produto()  # Chama a função para cadastrar um novo produto
                    elif opcao_admin == '2':
                        print("Logout realizado.")
                        break
                    else:
                        print("Opção inválida.")
        
        elif opcao == '4':
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida.")
