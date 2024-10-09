'''

Objetivo: Criar um sistema básico de gerenciamento de funcionários utilizando POO, aplicando os conceitos de herança e polimorfismo.

'''


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibirInfo(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: {self.salario}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def exibirInfo(self):
        super().exibirInfo()
        print(f"Bônus: {self.bonus}")
        print(f"Salário Total: {self.bonus + self.salario}")

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def exibirInfo(self):
        super().exibirInfo()
        print(f"Linguagem Principal: {self.linguagem}")


funcionarios = [
    Gerente("João Silva", 5000, 2000),
    Desenvolvedor("Maria Oliveira", 4000, "Python"), 
    Gerente("Murilo", 5500, 1)
]

for funcionario in funcionarios:
    funcionario.exibirInfo()
    print() 