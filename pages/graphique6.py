import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class Graphique6(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)


        main_frame = tk.Frame(self, bg='red')  # Fond rouge pour debug
        main_frame.pack(fill='both', expand=True)
        

        