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

        ttk.Label(self.header, text="Prix moyen", font=("Arial", 20), background=COLORS["primary"]).place(relx=0.5, y=10, anchor='n')  
        ttk.Button(self.header, text="Retour à l'accueil", command=lambda : controller.show_pages(Accueil)).place(relx=0.1, y=10, anchor='n')  
        
        self.main_frame = tk.Frame(self, width=450, height=600)
        self.main_frame.place(y=0)
        self.main_frame.lower()

        ttk.Label(self.main_frame, text="Quelques options pour le graphiques", font=("Arial", 15)).place(anchor="nw", x=10, y=60)

        self.srv = tk.BooleanVar()
        tk.Checkbutton(self.main_frame, text="Ajouter service -1", variable=self.srv).place(anchor="nw", x=30, y=110)


        self.toggle_button = ttk.Button(self.main_frame, text="Afficher le graphique", command=self.creation_graph)
        self.toggle_button.place(x=30 ,y=550)
        ttk.Button(self.main_frame, text="Télécharger le PDF", command=self.creation_graph, state=DISABLED).place(x=220 ,y=550)

        self.frame = tk.Frame(self)
        self.frame.place(relheight=1, y=0, x=450)
        self.frame.lower()

    def creation_graph(self):
        if self.figure:
            # Si le graphique est affiché, on le supprime
            if self.canvas_widget:
                self.canvas_widget.destroy()
            self.figure = False
            self.toggle_button.configure(text="Afficher le graphique")
        else:
            # Si pas de graphique, on le crée


            if (self.srv.get()): self.supp = None
            else: self.supp="-1"


            plt.figure()
            graph2(self.controller.x, col="SERVICE", supp=self.supp)
            plt.gcf().set_size_inches(5, 4)
            plt.tight_layout()
            plt.subplots_adjust(bottom=0.20)
            plt.savefig("./graphiques/img/test")
            
            # Créer et afficher le canvas
            canvas = FigureCanvasTkAgg(plt.gcf(), self.frame)
            canvas.draw()
            self.canvas_widget = canvas.get_tk_widget()
            self.canvas_widget.pack(side="right")
            
            self.figure = True
            self.toggle_button.configure(text="Supprimer le graphique")