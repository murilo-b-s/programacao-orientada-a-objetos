'''

Objetivo: Criar uma classe que represente um Retângulo, com métodos para calcular a área e o perímetro.

'''

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcularArea(self):
        if self.largura and self.altura > 1:
            return self.largura * self.altura
        else:
            print("Um dos valores não foi informado ou é negativo\n")
                
            

    def calcularPerimetro(self):
        if self.largura and self.altura > 1:
            return 2*(self.largura + self.altura)
        else:
            print("Um dos valores não foi informado ou é negativo")

largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))


forma = Retangulo(largura, altura)

print(f"A área do retângulo é: {forma.calcularArea()} ")
print(f"O perímetro do retângulo é: {forma.calcularPerimetro()} ")