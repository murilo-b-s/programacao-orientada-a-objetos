'''1. 
**Classe Base - Veiculo:**
   - Crie uma classe chamada `Veiculo` que tenha os seguintes atributos:
     - `marca` (string)
     - `modelo` (string)
     - `ano` (inteiro)
     - `preco_diaria` (float)
   - A classe deve ter um método chamado `calcular_aluguel` que recebe o número de dias e retorna o valor total do aluguel.
2. **Classe Derivada - Carro:**
   - Crie uma classe chamada `Carro` que herda de `Veiculo`.
   - Adicione um atributo adicional chamado `numero_portas` (inteiro).
   - Sobrescreva o método `calcular_aluguel` para aplicar um desconto de 10% se o aluguel for por mais de 7 dias.
3. **Classe Derivada - Moto:**
   - Crie uma classe chamada `Moto` que herda de `Veiculo`.
   - Adicione um atributo adicional chamado `cilindrada` (inteiro).
   - Sobrescreva o método `calcular_aluguel` para aplicar uma taxa adicional de 5% devido ao seguro de acidentes.
**Instruções:**
1. Implemente as classes `Veiculo`, `Carro` e `Moto` conforme especificado.
2. Crie instâncias de `Carro` e `Moto` e demonstre o uso de seus métodos, incluindo o cálculo do valor do aluguel.
3. Certifique-se de que os métodos sobrescritos considerem os cálculos adicionais (desconto para carros e taxa adicional para motos).
'''


class Veiculo:
    def __init__(self, marca, modelo, ano, precoDiario):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.precoDiario = precoDiario
        self.valor = None
        
    def calcularAluguel(self, dias):
        self.valor = dias * self.precoDiario
        return self.valor
    
    def listar(self):
        print('#####################################')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print(f'Preço diário: {self.precoDiario}')
        print(f'Valor total: {self.valor}\n')
        
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, precoDiario, numeroPortas):
        super().__init__(marca, modelo, ano, precoDiario)
        self.numeroPortas = numeroPortas
        
    def calcularAluguel(self, dias):
        super().calcularAluguel(dias)
        if dias > 7:
            self.valor = self.valor - (self.valor * 0.1)
            self.listar()
            
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, precoDiario, cilindrada):
        super().__init__(marca, modelo, ano, precoDiario)
        self.cilindrada = cilindrada
        
    def calcularAluguel(self, dias):
        super().calcularAluguel(dias)
        self.valor += (self.valor * 0.05)
        self.listar()
        
        
carro1 = Carro("ford", "gol", 2016, 100, 4)
carro1.calcularAluguel(8)

moto1 = Moto("honda", "aaaaa", 2016, 100, 150)
moto1.calcularAluguel(8)


