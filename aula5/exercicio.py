from datetime import datetime, timedelta


class Caminhao:
    def __init__(self, modelo, placa, capacidade):
        self.modelo = modelo
        self.placa = placa
        self.capacidade = capacidade
        self.peso = 0
        self.motorista = None

    def carregar(self, peso):
        while True:
            self.peso = peso
            if self.peso > self.capacidade or self.peso < 1:
                print("Essa carga não pode ser carregada neste caminhão")
            else:
                print("Carga carregada com sucesso!")
                break

    def descarregar(self, peso):
        while True:
            cargaParaDescarregar = int(input("Digite o valor que deseja descarregar: "))
            self.peso = peso - cargaParaDescarregar
            if self.peso < 0:
                print("Não tem como descarregar mais do que tem no caminhão")
            else:
                print(f"Foi descarregado {cargaParaDescarregar}")
                break

class Motorista:
    def __init__(self, nome, idade, cnh, dataValidade):
        self.nome = nome
        self.idade = idade
        self.cnh = cnh
        self.dataValidade = dataValidade
        self.caminhoes = []

    def dirigir(self, caminhao):
        if self.verificarValidade():
            caminhao.motorista = self
            self.caminhoes.append(caminhao)
            print(f"{self.nome} está dirigindo o caminhão {caminhao.modelo}")
        else: 
            print(f"{self.nome} não pode dirigir. CNH vencida")

    def verificarValidade(self):
        hoje = datetime.now().date()
        if self.dataValidade < hoje:
            print(f"A cnh de {self.nome} está vencida!")
            return False
        elif self.dataValidade <= hoje + timedelta(days=30):
            print(f"A CNH de {self.nome} vencerá logo. Renove.")
            return True
        else:
            print("Validade dentro do praso")
            return True



def imprimirInfo(caminhao):
    print(f"Caminhão:")
    print(f" Modelo: {caminhao.modelo}")
    print(f" Placa: {caminhao.placa}")
    print(f" Placa: {caminhao.placa}")
    print(f" Placa: {caminhao.placa}")
    print(f" Peso Atual: {caminhao.peso}")






modelo = input("Digite o modelo do caminhão: ")
placa = input("Digite a placa: ")
capacidade = int(input("Digite a capacidade de carga: "))
peso = int(input("Digite o peso da carga: "))

caminhao = Caminhao(modelo, placa, capacidade)



nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
cnh = int(input("Diite a sua cnh: "))
dataValidade = input("Digite a validade da cnh dd/mm/aaaa:  ")

motorista = Motorista(nome, idade, cnh, dataValidade)


caminhao.carregar(peso)
caminhao.descarregar(peso)
motorista.verificarValidade()
imprimirInfo(caminhao)

