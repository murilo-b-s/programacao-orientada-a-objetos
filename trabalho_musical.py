from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
import getpass


DATABASE_URL = "mysql+mysqlconnector://root:@localhost/lojamusica"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'

    ID_usuarios = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)

class Produtos(Base):
    __tablename__ = 'produtos'

    ID_produto = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(50), nullable=False)
    cor = Column(String(50), nullable=False)
    estoque = Column(Integer, nullable=False)
    valor = Column(Float, nullable=False)


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


cadastrar_usuario()
login()