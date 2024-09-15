class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.proprietario = None

    def definirProprietario(self, pessoa):
        self.proprietario = pessoa
        
    def mostrarInformacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        
        if self.proprietario:
            print(f"Proprietário: {self.proprietario.nome}")
            print(f"Idade: {self.proprietario.idade}")
        
        else:
            print(f"SEM PROPRIETÁRIO")
        
class Proprietario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.carros = []

    def addCarro(self, carro):
        self.carros.append(carro)
        carro.definirProprietario(self)

    def mostrarInformacoes(self):
        print(f'Nome: {self.nome}')
        print(f'idade: {self.idade}')
        print(f'\nCarros:')
        for carro in self.carros:
            carro.mostrarInformacoes()


proprietarios = []
carros = []

while True:
    print(f'''{"="*20}
            1 = Criar proprietário
        {"="*20}''')
    escolha = input()
    if escolha == '1':
        nomePessoa = input("Digite o nome do proprietário: ").capitalize()
        idadePessoa = input("Digite a idade do proprietário: ")
        pessoa = Proprietario(nomePessoa, idadePessoa)
        proprietarios.append(pessoa.nome)
        print(proprietarios)
        adicionar_carro = input(f"Gostaria de adicionar um carro à lista de {pessoa.nome}? ")

    if escolha == '2':

        pass

    if escolha == '0':
        break




        
# marca = input("Digitite a marca do carro: ")
# modelo = input("Digitite o modelo do carro: ")
# ano = input("Digitite o ano do carro: ")

# carro = Carro(marca, modelo, ano)
# carro.mostrarInformacoes()

# nomePessoa = input("Digite o nome do proprietário: ")
# idadePessoa = input("Digite a idade do proprietário: ")
# pessoa = Proprietario(nomePessoa, idadePessoa)

# carro.mostrarInformacoes()

# carro.definirProprietario(pessoa)
# carro.mostrarInformacoes()




