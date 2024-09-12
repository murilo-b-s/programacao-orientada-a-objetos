class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.proprietario = None

    def definirProprietario(self, pessoa):
        
        self.proprietario = pessoa
        
    def mostrarInformacoes(self):
        info = (f'''
Marca: {self.marca}
Modelo: {self.modelo}
Ano: {self.ano}
            ''')
        
        if self.proprietario:
            info += f"\nProprietário: {self.proprietario.nome}"
            info += f"\nIdade: {self.proprietario.idade}"
        
        else:
            info += "\nSEM PROPRIETÁRIO"
        print(info)
        
class Proprietario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
        


        
marca = input("Digitite a marca do carro: ")
modelo = input("Digitite o modelo do carro: ")
ano = input("Digitite o ano do carro: ")

carro = Carro(marca, modelo, ano)
carro.mostrarInformacoes()

nomePessoa = input("Digite o nome do proprietário: ")
idadePessoa = input("Digite a idade do proprietário: ")
pessoa = Proprietario(nomePessoa, idadePessoa)

carro.mostrarInformacoes()

carro.definirProprietario(pessoa)
carro.mostrarInformacoes()




