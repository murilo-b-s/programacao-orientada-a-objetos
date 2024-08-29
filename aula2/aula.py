
import pygame

import sys


class Automovel:
    def __init__(self, marca, modelo, cilindrada, num_portas, cor):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.num_portas = num_portas
        self.cor = cor
        self.velocidade = 0  # Inicializa a velocidade como zero
        self.sentido = None
        self.marcha = 1
        
    def acelerar(self):
        if self.sentido == True:
            self.velocidade += 10
            print(f"O automóvel {self.marca} {self.modelo} acelerou e está indo para frente. Velocidade atual: {self.velocidade} km/h")
        elif self.sentido == False:
            self.velocidade += 1
            print(f"O automóvel {self.marca} {self.modelo} acelerou e está indo para trás. Velocidade atual: {self.velocidade} km/h")
            
    def frear(self):
        if self.sentido == True:
            self.velocidade -= 10
            print(f"O automóvel {self.marca} {self.modelo} freou. Velocidade atual: {self.velocidade} km/h")
        elif self.sentido == False:
            self.velocidade -= 1
            print(f"O automóvel {self.marca} {self.modelo} acelerou. Velocidade atual: {self.velocidade} km/h")
        else:
            print("O automóvel já está parado.")
    def parar(self):
        self.velocidade = 0
        print(f"O automóvel {self.marca} {self.modelo} parou. Velocidade atual: {self.velocidade} km/h")
        
    def situacao(self):
        if self.velocidade > 0:
            print(f"O {self.modelo} está andando")
        else:
            print(f"O {self.marca} está parado")
            
    def mudar_marcha(self):
        str(input("Digite a marcha que o carro está: ")).upper
        if self.marcha in ('1', '2', '3', '4', '5'):
            self.sentido == True
        elif self.marcha == "R":
            self.velocidade = 0
            self.sentido == False
            
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Controle do Carro")

# Cria um objeto da classe Automovel
carro1 = Automovel("Toyota", "Corolla", 2000, 4, "Prata")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                carro1.acelerar()
                
    screen.fill((0, 0, 0))  # Limpa a tela com a cor preta
    pygame.display.flip()  


# Exemplo de inicialização de objetos e uso dos métodos
carro1 = Automovel("Toyota", "Corolla", 2000, 4, "Prata")
carro2 = Automovel("Honda", "Civic", 1800, 4, "Preto")



carro1.mudar_marcha()
carro1.acelerar()
carro1.situacao()

carro1.frear()
carro1.situacao()
    
    
# carro1.acelerar()
# carro1.acelerar()
# carro1.frear()
# carro1.parar()
# carro2.acelerar()
# carro2.frear()
# carro2.frear()
# carro2.parar()