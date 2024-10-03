from animal import Animal

class Passaro(Animal):
    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade)
        self.especie = especie

    def cantar(self):
        print(f"{self.nome} está cantando!")