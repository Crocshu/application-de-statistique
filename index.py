import tkinter as tk 
from tkinter import ttk 
from pages.page1 import Page1
from pages.page2 import Page2
from config import WINDOW_SIZE

class index(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Application Graphiques")
        self.geometry(WINDOW_SIZE)

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.pages = {}
        for Page in (Page1, Page2):
            page = Page(self.container, self)
            self.pages[Page] = page
            page.grid(row=0, column=0, sticky="nsew")
        
        self.show_page(Page1)

    def show_page(self, page_class):
        page = self.pages[page_class]
        page.tkraise()


app = index()
app.mainloop()