import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graphiques.niv1 import *
from config import COLORS

class Graphique1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.figure = False
        self.controller = controller

        header = ttk.Style()
        header.configure("Header.TFrame", background=COLORS["primary"], borderwidth=2, relief='solid')
        self.header = ttk.Frame(self, style="Header.TFrame", height=50)
        self.header.place(x=0, y=0, relwidth=1)

        ttk.Label(self.header, text="Prix moyen", font=("Arial", 20), background=COLORS["primary"]).place(relx=0.5, y=10, anchor='n')
        self.toggle_button = ttk.Button(self.header, text="Afficher le graphique", command=self.creation_graph)
        self.toggle_button.place(relx=0.1, y=10, anchor='n')
    
        
        self.main_frame = tk.Frame(self, width=450)
        self.main_frame.place(y=0, relheight=1)
        self.main_frame.lower()

        srv = False 

        self.radio = tk.Checkbutton(self, text="Ajouter service -1", variable=srv)
        self.radio.place(anchor="nw", y=60)

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
            plt.figure()
            graph1(self.controller.x)
            plt.gcf().set_size_inches(5, 4)
            plt.tight_layout()
            plt.subplots_adjust(bottom=0.30)
            
            # Créer et afficher le canvas
            canvas = FigureCanvasTkAgg(plt.gcf(), self.frame)
            canvas.draw()
            self.canvas_widget = canvas.get_tk_widget()
            self.canvas_widget.pack(side="right")
            
            self.figure = True
            self.toggle_button.configure(text="Supprimer le graphique")