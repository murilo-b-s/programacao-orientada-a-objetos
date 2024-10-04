




import json

CAMINHO_ARQUIVO = 'aula206_207.json'

class Pessoa:
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), vars(p2), vars(p3)]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)