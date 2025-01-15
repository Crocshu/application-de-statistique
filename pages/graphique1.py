import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from graphiques.niv1 import graph1
from config import COLORS

class Graphique1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        
        header = ttk.Style()
        header.configure("Header.TFrame", background=COLORS["primary"], borderwidth=2, relief='solid')
        self.header = ttk.Frame(self, style="Header.TFrame", height=50)
        self.header.place(x=0, y=0, relwidth=1)

        ttk.Label(self.header, text="Prix moyen", font=("Arial", 20), background=COLORS["primary"]).place(relx=0.5, y=10, anchor='n')


        def creation_graph (graph):
            print(f"graphique : {graph}")

        creation_graph(graph1)