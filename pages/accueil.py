import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

from config import COLORS, ecran

class Accueil(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        header = ttk.Style()
        header.configure("Header.TFrame", background=COLORS["primary"], borderwidth=2, relief='solid')
        self.header = ttk.Frame(self, style="Header.TFrame", height=100)
        self.header.place(x=0, y=0, relwidth=1)


        ttk.Label(self.header, text="ARNAIZ Tristan", font=("Arial", 12), background=COLORS["primary"]).place(x=20, y=10)
        ttk.Label(self.header, text="LAMY Nathan", font=("Arial", 12), background=COLORS["primary"]).place(relx=1, y=10, x=-20, anchor='ne')
        ttk.Label(self.header, text="SAE 105 / Graphiques", font=("Arial", 20), background=COLORS["primary"]).place(relx=0.5, y=30, anchor='n')

        self.contenu = ttk.Frame(self)
        self.contenu.pack(expand=True, padx=10, pady=110, anchor="center") # padx & pady servent a ajouter des marges extérieures

        title = ttk.Label(self.contenu, text="Nos types de graphiques", font=("Arial", 20))
        title

        self.illustrations = []
        for i in range(1, 7):
            img = f"./graphiques/img/graph{i}.png"
            photo = PhotoImage(file=img)
            photo = photo.subsample(3, 3)
            self.illustrations.append(photo)

        self.nom_graph = ["Prix moyen", 
                          "Nombre mouvement / Services", 
                          "Mouvement par mois 4 principaux services", 
                          "Proportion mouvement / Services",
                          "Proportion de mouvements / mouvement et par jour",
                          "Evolution du prix des 4 produites + vendus"]
        
        from pages.graphique1 import Graphique1
        from pages.graphique2 import Graphique2
        from pages.graphique3 import Graphique3
        from pages.graphique4 import Graphique4
        from pages.graphique5 import Graphique5
        from pages.graphique6 import Graphique6

        self.graph = [Graphique1,
                      Graphique2,
                      Graphique3,
                      Graphique4,
                      Graphique5,
                      Graphique6]

        for i in range(2):  # Lignes
            for j in range(3):  # Colonnes
                index = i * 3 + j
                frame = ttk.Frame(self.contenu)
                frame.grid(row=i, column=j, padx=15, pady=10, sticky="nsew")
                
                page = self.graph[index]
                
                # Bouton avec image
                btn = ttk.Button(
                    frame,
                    text=self.nom_graph[index],
                    image=self.illustrations[index],
                    compound=TOP,
                    command=lambda p=page: controller.show_page(p)
                )
                btn.pack(expand=True)

