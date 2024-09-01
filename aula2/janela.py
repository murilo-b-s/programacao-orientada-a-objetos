#####################################
# Cálculo IMC com Janela
#
import tkinter as tk
from tkinter import messagebox
def calcular_imc():
    """Calcula o IMC com base nos valores inseridos e exibe o resultado."""
    altura = float(entry_altura.get())
    peso = float(entry_peso.get())
    imc = peso / (altura ** 2)
    messagebox.showinfo("Resultado", f"Seu IMC é: {imc:.2f}")
# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry('300x150')
# Rótulos e campos de entrada
label_altura = tk.Label(janela, text="Altura (m):")
label_altura.pack()
entry_altura = tk.Entry(janela)
entry_altura.pack()
label_peso = tk.Label(janela, text="Peso (kg):")
label_peso.pack()
entry_peso = tk.Entry(janela)
entry_peso.pack()
# Botão para calcular
botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.pack()
# Iniciando a aplicação
janela.mainloop()

############################################# 
# CÁLCULO DO IMC SEM JANELA
#
while True: #Controla o Programa
    while True: #Controla entrada altura
        try:
            altura=float(input("Altura (m):"))
            while altura<.30 or altura > 2.72:
                altura=float(input("Altura (m):"))
            break
        except:
            print("Altura deve ser Float")
    while True: # controla entrada peso
        try:
            peso=float(input("Peso (kg):"))
            break
        except:
            print("Peso devem ser Float")
    print(f"IMC={peso/altura**2:.2f}")
    continua=input("Continua (S/N)?")
    while continua.upper()!='N' and continua.upper()!='S':
        print("Digite SOMENTE (S/N)!")
        continua=input("Continua (S/N)?")
    if continua.upper()=='N':
        break
print("fim do Programa")