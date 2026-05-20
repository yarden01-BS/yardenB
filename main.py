import tkinter as tk
from view import ConnexionEcran
from controller import ControllerConnexion

fenetre = tk.Tk()
fenetre.geometry("750x550")
fenetre.title("Connexion Sécurisée - GESTIONDR1")
fenetre.configure(bg="#1e1e2e")
connexion_ecran = ConnexionEcran(fenetre)
connexion_ecran.place(relx=0.5, rely=0.5, anchor="center", width=650, height=350)
fenetre.mainloop()
