class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        pass  # Implementar em cada classe filha

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        print(f"{self.nome} está latindo!")

class Gato(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor

    def emitir_som(self):
        print(f"{self.nome} está miando!")

class Passaro(Animal):
    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade)
        self.especie = especie

    def emitir_som(self):
        print(f"{self.nome} está cantando!")

# Criando objetos e utilizando métodos
cachorro = Cachorro("Rex", 3, "Labrador")
gato = Gato("Mia", 2, "Branco")
passaro = Passaro("Piu-Piu", 1, "Canario")

cachorro.emitir_som()
gato.emitir_som()
passaro.emitir_som()