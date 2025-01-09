import tkinter as tk
from tkinter import ttk

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        ttk.Label(text="Test page1")