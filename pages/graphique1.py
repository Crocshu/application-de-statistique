import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import *
from graphiques.niv1 import *
from config import COLORS

class Graphique1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        
        header = ttk.Style()
        header.configure("Header.TFrame", background=COLORS["primary"], borderwidth=2, relief='solid')
        self.header = ttk.Frame(self, style="Header.TFrame", height=50)
        self.header.place(x=0, y=0, relwidth=1)

        ttk.Label(self.header, text="Prix moyen", font=("Arial", 20), background=COLORS["primary"]).place(relx=0.5, y=10, anchor='n')
        ttk.Button(self.header, text="Afficher le graphique", command=lambda : creation_graph()).place(relx=0.1, y=10, anchor='n')

        x=of(ezip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=1000000000,separator=";",pandas=False)


        def creation_graph():
            graph1(x,"DATEMVT","VALHT",'Prix moyen des mouvements par mois')

            # Créer et afficher le graphique
            plt.gcf().set_size_inches(5, 4)  # Modifiez ces valeurs pour changer la taille

            # Ajuster les marges pour tout voir
            plt.tight_layout()
            plt.subplots_adjust(bottom=0.35) 
            # Créer le canvas
            canvas = FigureCanvasTkAgg(plt.gcf(), self)
            canvas.draw()
            canvas.get_tk_widget().pack(side="bottom", anchor="s")    
