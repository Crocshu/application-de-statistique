import tkinter as tk
from tkinter import ttk
from pages.page2 import Page2
from config import COLORS, ecran

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        header = ttk.Style()
        header.configure("Header.TFrame", background=COLORS["primary"], borderwidth=2, relief='solid')

        self.header = ttk.Frame(style="Header.TFrame", height=100).place(x=0,y=0, width=ecran.width)
        ttk.Label(self.header, text="ARNAIZ Tristan", font=("Arial", 12), background=COLORS["primary"]).place(x=20, y=10)
        ttk.Label(self.header, text="LAMY Nathan", font=("Arial", 12), background=COLORS["primary"]).place(x=1, anchor="e")