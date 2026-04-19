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


        self.frame_btn = ctk.CTkFrame(self)
        self.frame_btn.pack(pady=10)

        ctk.CTkButton(self.frame_btn, text="Ajouter").grid(row=0, column=0)
        ctk.CTkButton(self.frame_btn, text="Modifier").grid(row=0, column=1)
        ctk.CTkButton(self.frame_btn, text="Supprimer").grid(row=0, column=2)
        ctk.CTkButton(self.frame_btn, text="Rechercher").grid(row=0, column=3)

        from tkinter import ttk

        self.tree = ttk.Treeview(self, columns=("code", "libelle", "type", "capacite"), show="headings")

        self.tree.heading("code", text="Code")
        self.tree.heading("libelle", text="Libelle")
        self.tree.heading("type", text="Type")
        self.tree.heading("capacite", text="Capacite")

        self.tree.pack(fill="both", expand=True)

        from services.services_salle import ServiceSalle

        self.service = ServiceSalle()

        from models.salle import Salle

        def ajouter(self):
            s = Salle(
                self.code.get(),
                self.libelle.get(),
                self.type.get(),
                int(self.capacite.get())
            )
            self.service.ajouter_salle(s)
            self.lister()

        def modifier(self):
            s = Salle(
                self.code.get(),
                self.libelle.get(),
                self.type.get(),
                int(self.capacite.get())
            )
            self.service.modifier_salle(s)
            self.lister()

        def supprimer(self):
            self.service.supprimer_salle(self.code.get())
            self.lister()

        def rechercher(self):
            s = self.service.rechercher_salle(self.code.get())

            if s:
                self.code.delete(0, "end")
                self.code.insert(0, s.code)

                self.libelle.delete(0, "end")
                self.libelle.insert(0, s.libelle)

                self.type.delete(0, "end")
                self.type.insert(0, s.type)

                self.capacite.delete(0, "end")
                self.capacite.insert(0, s.capacite)