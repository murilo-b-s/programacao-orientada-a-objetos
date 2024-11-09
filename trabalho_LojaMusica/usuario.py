from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
# from main import session
from produtos import Produtos

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'

    ID_usuarios = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)

    def comprar(self):

        from main import  session

        categoria = input('Produto desejado: ')
        cor = input('Cor do produto desejado: ')

        produto_encontrado = session.query(Produtos).filter_by(categoria = categoria, cor = cor).first()
        if produto_encontrado:
            if produto_encontrado.estoque > 0:
                print('Produto disponível. Realizando compra...')
                produto_encontrado.estoque -= 1
                
                session.commit()
                print(f"Compra realizada com sucesso!")
        else:
            print('Produto fora de estoque')