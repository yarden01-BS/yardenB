import tkinter as tk

class GestionEcran(tk.Frame):
    def __init__(self, parent: tk.Tk, controller):
        super().__init__(parent, bg="#1e1e2e")
        self.controller = controller
