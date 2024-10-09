'''

Objetivo: Criar um sistema de gerenciamento de livros em uma biblioteca, utilizando herança e polimorfismo.

'''


class ItemBiblioteca:
    def __init__(self, titulo, anoPublicacao):
        self.titulo = titulo
        self.anoPublicacao = anoPublicacao

    def exibirInfo(self):
        print(f'Título: {self.titulo}')
        print(f'Ano de Publicação: {self.anoPublicacao}')

class Livros(ItemBiblioteca):
    def __init__(self, titulo, anoPublicacao, autor, numeroPaginas):
        super().__init__(titulo, anoPublicacao)
        self.autor = autor
        self.numeroPaginas = numeroPaginas

    def exibirInfo(self):
        super().exibirInfo()
        print(f'Autor: {self.autor}')
        print(f'Número de páginas: {self.numeroPaginas}')
        

class Revista(ItemBiblioteca):
    def __init__(self, titulo, anoPublicacao, edicao, mesPublicacao):
        super().__init__(titulo, anoPublicacao)
        self.edicao = edicao
        self.mesPublicacao = mesPublicacao

    def exibirInfo(self):
        super().exibirInfo()
        print(f'Edição: {self.edicao}')
        print(f'Mês de publicação: {self.mesPublicacao}')


itens = [
    Livros("O Pequeno Príncipe", 1954, "Shakespeare", 140), 
    Revista("Veja", 2018, 9, "Outubro"),
    Livros("O Último Homem", 2007, "Mateus", 55),
    Revista("O Mundo Mágico", 2006, 34, "Janeiro")
]

for item in itens:
    item.exibirInfo()
    print()