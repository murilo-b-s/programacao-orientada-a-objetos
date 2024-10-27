from model import create_tables, Session, Pet

class PetController:
    def __init__(self, view):
        self.view = view
        self.session = Session()
        self.view.button_add.config(command=self.add_pet)
        self.view.button_show.config(command=self.show_pets)
        self.view.button_adopt.config(command=self.adopt_pet)
        self.view.button_limpar.config(command=self.limpa_area)

    def add_pet(self):
        if self.view.entry_name.get() and self.view.entry_age.get() and self.view.entry_species.get():
            try:
                name = self.view.entry_name.get()
                age = int(self.view.entry_age.get())
                species = self.view.entry_species.get()
                print(name, age, species)
                new_pet = Pet(name=name, age=age, species=species)
                self.session.add(new_pet)
                self.session.commit()
                self.view.clear_entries()
            except ValueError:
                self.view.show_error("Por favor, insira uma idade válida!")
        else:
            self.view.show_error("Por favor, preencha todos os campos.")
    def adopt_pet(self):
        selected_pet_name = self.view.get_selected_pet_name()
        if selected_pet_name:
            pet = self.session.query(Pet).filter_by(name=selected_pet_name).first()
            if pet:
                pet.adopted = True  # Atualiza o status para adotado
                self.session.commit()
                self.view.show_pets(self.session.query(Pet).all())  # Atualiza a lista de pets
                self.view.show_error(f"{pet.name} foi adotado com sucesso!")
            else:
                self.view.show_error("Pet não encontrado.")
        else:
            self.view.show_error("Por favor, selecione um pet para adotar.")


    def show_pets(self):
        pets = self.session.query(Pet).all()
        self.view.show_pets(pets)

    def limpa_area(self):
       self.view.limpa_area()
