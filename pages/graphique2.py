import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graphiques.niv2 import *
from pages.accueil import Accueil
from config import COLORS

class Graphique2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.figure = False
        self.controller = controller

        header = ttk.Style()
        header.configure("Header.TFrame", background=COLORS["primary"], borderwidth=2, relief='solid')
        self.header = ttk.Frame(self, style="Header.TFrame", height=50)
        self.header.place(x=0, y=0, relwidth=1)

        ttk.Label(self.header, text="Nombre de mouvements par service", font=("Arial", 20), background=COLORS["primary"]).place(relx=0.5, y=10, anchor='n')  
        ttk.Button(self.header, text="Retour à l'accueil", command=lambda : self.controller.show_page(Accueil)).place(relx=0.1, y=10, anchor='n')  
        
        self.main_frame = tk.Frame(self, width=450, height=600)
        self.main_frame.place(y=0)
        self.main_frame.lower()

        ttk.Label(self.main_frame, text="Quelques options pour le graphiques", font=("Arial", 15)).place(anchor="nw", x=10, y=60)

        self.title = tk.StringVar()
        ttk.Label(self.main_frame, text="Titre du graphique (laissez vide pour le titre par défaut).", font=("Arial", 11)).place(anchor="nw", x=30, y=110)
        ttk.Entry(self.main_frame, textvariable=self.title, width=38).place(anchor="nw", x=30, y=130)

        self.choixcouleur = tk.StringVar()
        self.couleurs = {"Orange":"orange", "Rouge":"red", "Bleu":"blue", "Vert":"green",  "Violet":"purple"}
        ttk.Label(self.main_frame, text="Selectionnez la couleur du graphiques", font=("Arial", 11)).place(anchor="nw", x=30, y=170)
        ttk.OptionMenu(self.main_frame, self.choixcouleur, list(self.couleurs.keys())[0],*self.couleurs.keys()).place(anchor="nw", x=30, y=190)

        self.nb_services = tk.IntVar(value=15)
        ttk.Label(self.main_frame, text="Sélectionnez le nombre de services", font=("Arial", 11)).place(anchor="nw", x=30, y=240)
        ttk.Spinbox(self.main_frame, from_=1, to=20,  # Augmenté pour permettre la valeur 15
                    textvariable=self.nb_services, width=5).place(anchor="nw", x=30, y=260)

        self.srv = tk.BooleanVar()
        tk.Checkbutton(self.main_frame, text="Ajouter service -1", variable=self.srv).place(anchor="nw", x=25, y=310)

        self.toggle_button = ttk.Button(self.main_frame, text="Afficher le graphique", command=self.creation_graph)
        self.toggle_button.place(x=30 ,y=550)
        ttk.Button(self.main_frame, text="Télécharger le PDF", command=self.creation_graph, state=DISABLED).place(x=220 ,y=550)

        self.frame = tk.Frame(self)
        self.frame.place(relheight=1, y=0, x=450)
        self.frame.lower()

    def creation_graph(self):
        # Nettoyage de la figure actuelle
        plt.clf()
        couleur_selec = self.couleurs[self.choixcouleur.get()]
        nbr_srv = self.nb_services.get()

        # Création du nouveau graphique
        if (self.srv.get()): self.supp = None
        else: self.supp = "-1"

        graph2v2(self.controller.df, supp=self.supp, nbr=nbr_srv,couleur=couleur_selec)
        if self.title.get() != "" : plt.title(self.title.get())
        plt.gcf().set_size_inches(5, 4)
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.20)
        plt.savefig("./graphiques/img/g2.png")

        # Gestion du canvas
        if not hasattr(self, 'canvas'): # hasattr (has attribute), sert à vérifier si self, possède l'attribut canvas
            # Première création
            self.canvas = FigureCanvasTkAgg(plt.gcf(), self.frame)
            self.canvas_widget = self.canvas.get_tk_widget()
            self.canvas_widget.pack(side="right")
            self.figure = True
        else:
            # Mise à jour
            self.canvas.figure = plt.gcf()
            self.canvas.draw()

        self.toggle_button.configure(text="Actualiser le graphique")