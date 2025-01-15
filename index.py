import tkinter as tk 
from tkinter import ttk 
from pages.page1 import Page1
from pages.graphique1 import Graphique1
from pages.graphique2 import Graphique2
from pages.graphique3 import Graphique3
from pages.graphique4 import Graphique4
from pages.graphique5 import Graphique5
from pages.graphique6 import Graphique6

from config import WINDOW_SIZE

class index(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Application Graphiques")
        self.geometry(WINDOW_SIZE)
        self.resizable(width=False, height=False)
        
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)


        self.pages = {}
        for Page in (Page1, Graphique1, Graphique2, Graphique3, Graphique4, Graphique5, Graphique6):
            page = Page(self.container, self)
            self.pages[Page] = page
            page.grid(row=0, column=0, sticky="nsew")
        
        self.show_page(Page1)

    def show_page(self, page_class):
        print(f"Affichage de la page {page_class.__name__}")  # Debug print
        page = self.pages[page_class]
        page.tkraise()


app = index()
app.mainloop()