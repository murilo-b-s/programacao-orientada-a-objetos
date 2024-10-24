import tkinter as tk
from model import create_tables
from view import PetView
from controller import PetController

def main():
    create_tables()  # Cria as tabelas no banco de dados
    root = tk.Tk()
    view = PetView(root)
    controller = PetController(view)
    root.mainloop()

if __name__ == "__main__":
    main()
