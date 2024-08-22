class Conta:
    def __init__(self, numero, saldo, nome):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        
        
    def listar(self):
        print("\n###################")
        print(f"Cliente: {self.nome}")
        print(f"Conta Corrente: {self.numero}")
        print(f"Saldo: {self.saldo}")
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        self.saldo -= valor
        
def entrada():
    nome = input("Digite o nome do cliente: ")
    numero = input("Digite a conta: ")
    saldo = float(input("Digite o saldo incial: "))
    return (nome, numero, saldo)
    
    
    
lst_clientes = []
lst_contas = []
lst_saldos = []


if __name__ == '__main__':
    nome,numero,saldo = entrada()
    # nome = input("Digite o nome do cliente: ")
    # numero = input("Digite a conta: ")
    # saldo = float(input("Digite o saldo incial: "))
    conta_murilo = Conta(numero, saldo, nome)
    conta_murilo.listar()
    # conta_murilo.numero = "1234-5"
    # conta_murilo.saldo = 503.45
    # conta_murilo.listar()

    nome, numero, saldo = entrada()
    conta_lucca = Conta(numero, saldo, nome)
    conta_lucca.listar()
    # conta_lucca = Conta()
    # conta_lucca.numero = "45312-5"
    # conta_lucca.saldo = 50000.00
    # conta_lucca.listar()
    
    
    # conta_gusta = Conta()
    # conta_gusta.numero = "77375-5"
    # conta_gusta.saldo = 500000.00
    # conta_gusta.listar()
    
    
    # conta_cleber = Conta()
    # conta_cleber.numero = "49773-5"
    # conta_cleber.saldo = 5070.00
    # conta_cleber.listar()
    
    
    # conta_henrique = Conta()
    # conta_henrique.numero = "47487-5"
    # conta_henrique.saldo = 1000.00
    # conta_henrique.listar()
    
    
    # conta_lisi = Conta()
    # conta_lisi.numero = "98378-5"
    # conta_lisi.saldo = 11.10
    # conta_lisi.listar()
    
    
    # conta_lisi.sacar(10)
    # conta_lucca.depositar(10)
    # conta_lucca.listar()
    # conta_lisi.listar()
    
    