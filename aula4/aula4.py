import random as rm

class AnimalEstimacao:
    def __init__(self, nome, especie, idade, tutor):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.estado = None
        self.tutor = tutor

    def comer(self):
        comendo = ["Comendo ração", "Comendo o resto do almoço", "Bebendo água"]
        self.estado = rm.choice(comendo)
            
    def dormir(self):
        dormindo = ["Dormindo na caminha", "Dormindo no sofá", "Dormindo no pátio"]
        self.estado = rm.choice(dormindo)

    def brincar(self):
        brincando = ["Brincando com a bolinha", "Brincando com o amiguinho", "Brincando com uma sacola"]
        self.estado = rm.choice(brincando)

    def pular(self):
        self.estado = "Pulando"
    
    def passear(self):
        passeando = ["Passeando no parque", "Passeando na praia", "Passeando no condomínio"]
        self.estado = rm.choice(passeando)

    def listar(self):
        print(f'''Nome: {self.nome}, Espécie: {self.especie}
            Idade: {self.idade} anos  
            Estado: {self.estado} 
            Tutor nome: {self.tutor.nome}
            Tutor celular: {self.tutor.celular}''')
        

    def randomizar_estado(self):
        acoes = [self.comer, self.dormir, self.brincar, self.pular, self.passear]
        acao_escolhida = rm.choice(acoes)
        acao_escolhida()
        
        
class Tutor:
    def __init__(self, nome, cpf, celular):
        self.nome = nome
        self.cpf = cpf
        self.celular = celular
        
    def listar(self):
        print("\n")
        print("*"*20, "Lista Tutor", "*"*20)
        print(f'''
            Nome: {self.nome}
            CPF: {self.cpf}
            Celular: {self.celular}
            ''')



# nome1 = Tutor("Murilo", "060.275.140-35", "(51)99839-7378")

# animal = AnimalEstimacao("Rex", "Cachorro", 3)
# animal.randomizar_estado()
# animal.listar()

nomeTutor = input("Digite o seu nome: ")
cpfTutor = input("Digite o seu cpf: ")
celularTutor = input("Digite o seu número de celular: ")

tutor = Tutor(nomeTutor, cpfTutor, celularTutor)

nome = input("Digite o nome do animal: ")
especie = input(f"Digite a especie do {nome}: ")
idade = input(f"Digite a idade do {nome}: ")

animal = AnimalEstimacao(nome, especie, idade, tutor)

menu = """
    ============================================
    Menu:
    0 para Sair
    1 para saber o que seu animal está fazendo
    ============================================"""
while True:
    print(menu)
    escolha = input("")
    if escolha == "0":
        break
    elif escolha == "1":
        animal.randomizar_estado()
        animal.listar()
    else:
        print("Escolha inválida")
