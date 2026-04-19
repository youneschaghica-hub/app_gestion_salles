import customtkinter as ctk

class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("800x600")


        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.pack(pady=10)

        self.code = ctk.CTkEntry(self.frame_info, placeholder_text="Code")
        self.code.grid(row=0, column=0)

        self.libelle = ctk.CTkEntry(self.frame_info, placeholder_text="Libelle")
        self.libelle.grid(row=0, column=1)

        self.type = ctk.CTkEntry(self.frame_info, placeholder_text="Type")
        self.type.grid(row=0, column=2)

        self.capacite = ctk.CTkEntry(self.frame_info, placeholder_text="Capacite")
        self.capacite.grid(row=0, column=3)