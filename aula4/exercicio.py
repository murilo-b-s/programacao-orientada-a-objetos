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

    def mostrarInfoSemProp(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}\n")
        
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
        print(f'Idade: {self.idade}')
        if self.carros == []:
            print(f"{self.nome} não possui nenhum carro")
        
        else:
            print(f'\nCarros:')
            for carro in self.carros:
                carro.mostrarInfoSemProp()

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'


def criar_proprietario():
    nomePessoa = input("Digite o nome do proprietário: ").capitalize()
    idadePessoa = input("Digite a idade do proprietário: ")
    pessoa = Proprietario(nomePessoa, idadePessoa)
    proprietarios.append(pessoa)
    pessoa.mostrarInformacoes()
    return pessoa

def criar_carro():
    marca = input("Digitite a marca do carro: ")
    modelo = input("Digitite o modelo do carro: ")
    ano = input("Digitite o ano do carro: ")
    carro = Carro(marca, modelo, ano)
    return carro

proprietarios = []
carros = []

while True:
    print(f'''{"="*20}
            1 = Criar proprietário
            2 = Criar carro
        {"="*20}''')
    escolha = input()

    if escolha == '1':
        pessoa = criar_proprietario()
        while True:
            adicionar_carro = input(f"Gostaria de adicionar um carro à lista de {pessoa.nome}? S/N ").upper()
            if adicionar_carro == "S":
                carro = criar_carro(pessoa)
                carros.append(carro)
                pessoa.addCarro(carro)
                pessoa.mostrarInformacoes()
                break
            if adicionar_carro == "N":
                break
            else:
                print("\nNão foi digitado S ou N\n")
                pass

    if escolha == '2':
        criar_carro()
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




