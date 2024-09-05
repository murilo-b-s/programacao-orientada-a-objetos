class Aluno:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina
        self.nota1 = 0
        self.nota2 = 0
        self.notaExame = None
        self.exame = None
        
        
    def lancarNota1(self):
        self.nota1 = float(input("Digite a sua primeira nota: "))
        
    def lancarNota2(self):
        self.nota2 = float(input("Digite a sua segunda nota: "))
        
    def mostarNotas(self):
        print(self.nota1)
        print(self.nota2)
        
    def situacao(self):
        if (self.nota1 + self.nota2)/2 >= 7:
            print("Você passou meu mestre!")
            self.exame = False
            
        else:
            print("Aluno com nota insuficiente!")
            self.exame = True
            return True
            
    def lancarExame(self):
        if self.exame == False:
            print("O aluno já está passado!")
            
        else:
            self.notaExame = float(input("Digite a nota da recuperação: "))
            
            
    def situacaoExame(self):
        if self.notaExame == None:
            print(f"{self.nome} não precisou de exame!")
        elif self.notaExame >= 7:
            print("Você passou meu mestre!")
        else:
            print("Aluno reprovado!")


aluno1 = Aluno("Murilo", "ADS")
aluno1.lancarNota1()
aluno1.lancarNota2()
aluno1.mostarNotas()
if aluno1.situacao() == True:
    aluno1.lancarExame()
    aluno1.situacaoExame()