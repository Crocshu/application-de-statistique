import tkinter as tk 
from tkinter import ttk 
from pages.accueil import Accueil
from pages.graphique1 import Graphique1
from pages.graphique2 import Graphique2
from pages.graphique3 import Graphique3
from pages.graphique4 import Graphique4
from pages.graphique5 import Graphique5
from pages.graphique6 import Graphique6
from graphiques.main import ouvrir_fichier as of
from config import WINDOW_SIZE

class Index(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Application Graphiques")
        self.geometry(WINDOW_SIZE)
        self.resizable(width=False, height=False)
        
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.df=of(ezip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=1000000000,separator=";",pandas=True)
        self.dfsp=of(ezip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=1000000000,separator=";")

        self.pages = {}

        for Page in (Accueil, Graphique1, Graphique2, Graphique3, Graphique4, Graphique5, Graphique6):
            page = Page(self.container, self)
            self.pages[Page] = page
            page.grid(row=0, column=0, sticky="nsew")
        
        self.show_page(Accueil)

    def show_page(self, page_class):
        print(f"Affichage de la page {page_class.__name__}")  # Debug print
        page = self.pages[page_class]
        page.tkraise()

if __name__ == "__main__":
    app = Index()
    app.mainloop()