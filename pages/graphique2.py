import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from config import COLORS

class Graphique2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        # Un label avec fond coloré pour le rendre plus visible
        label = tk.Label(self, 
                        text="Test graphique1",
                        bg="yellow",
                        font=("Arial", 14))
        label.pack(pady=20)
        
        # Un bouton pour vérifier si les widgets interactifs fonctionnent
        button = tk.Button(self, 
                          text="Cliquez-moi",
                          command=lambda: print("Bouton cliqué"))
        button.pack(pady=10)
        
        # Un cadre coloré pour voir les limites de la page
        frame_test = tk.Frame(self, 
                            bg="red",
                            width=200,
                            height=200)
        frame_test.pack(pady=10)