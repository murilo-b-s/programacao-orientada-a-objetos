import tkinter as tk
from tkinter import messagebox
class PetView:
    def __init__(self, master):
        self.master = master
        master.title("Pet Adoption")

        self.label_name = tk.Label(master, text="Nome:")
        self.label_name.pack()
        self.entry_name = tk.Entry(master)
        self.entry_name.pack()

        self.label_age = tk.Label(master, text="Idade:")
        self.label_age.pack()
        self.entry_age = tk.Entry(master)
        self.entry_age.pack()

        self.label_species = tk.Label(master, text="Espécie:")
        self.label_species.pack()
        self.entry_species = tk.Entry(master)
        self.entry_species.pack()

        self.button_add = tk.Button(master, text="Adicionar Pet")
        self.button_add.pack()

        self.button_show = tk.Button(master, text="Mostrar Pets")
        self.button_show.pack()

        self.button_adopt = tk.Button(master, text="Adotar Pet")
        self.button_adopt.pack()

        self.text_area = tk.Text(master)
        self.text_area.pack()

        self.button_limpar = tk.Button(master, text="Limpar")
        self.button_limpar.pack()

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_species.delete(0, tk.END)

    def show_pets(self, pets):
        self.text_area.delete(1.0, tk.END)  # Limpa a área de texto
        for pet in pets:
            self.text_area.insert(tk.END, f"Nome: {pet.name}, Idade: {pet.age}, Espécie: {pet.species}, Adotado: {'Sim' if pet.adopted else 'Não'}\n")
    def limpa_area(self):
        self.text_area.delete(1.0, tk.END)  # Limpa a área de texto
    def show_error(self, message):
        messagebox.showerror("Erro", message)

    def get_selected_pet_name(self):
        try:
            selected_text = self.text_area.selection_get()
            return selected_text.split(",")[0].split(":")[1].strip()  # Extrai o nome do pet
        except tk.TclError:
            return None  # Nenhum texto selecionado
