import sys
import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Canvas, CENTER
from tkinter import messagebox


class ConnexionEcran(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self._build()

    def _build(self):
        self.configure(
            bg="#2b2b3b",
            bd=0,
            highlightthickness=1,
            highlightbackground="#45475a",
        )
        self.label_titre = Label(
            self,
            text="CONNEXION",
            font=("Segoe UI", 18, "bold italic"),
            bg="#2b2b3b",
            fg="#89b4fa",
        )
        self.label_titre.place(relx=0.5, y=30, anchor=CENTER)
        self.canvas_photo = Canvas(
            self, width=180, height=180, bg="white", highlightthickness=0
        )
        self.canvas_photo.place(x=30, y=85)
        self.canvas_photo.create_oval(20, 20, 160, 160, fill="#0078d7", outline="")

        self.lbl_auth = Label(
            self,
            text="Authentification",
            font=("Segoe UI", 11, "italic"),
            bg="#2b2b3b",
            fg="#cdd6f4",
        )
        self.lbl_auth.place(x=240, y=75)

        Label(
            self,
            text="Utilisateur :",
            font=("Segoe UI", 10, "bold"),
            bg="#2b2b3b",
            fg="#89b4fa",
        ).place(x=240, y=110)

        self.entry_user = Entry(
            self,
            font=("Segoe UI", 11),
            bg="#313244",
            fg="white",
            bd=0,
            insertbackground="white",
        )
        self.entry_user.place(x=360, y=110, width=250, height=25)

        Label(
            self,
            text="Mot de passe :",
            font=("Segoe UI", 10, "bold"),
            bg="#2b2b3b",
            fg="#89b4fa",
        ).place(x=240, y=160)

        self.entry_pass = Entry(
            self,
            font=("Segoe UI", 11),
            bg="#313244",
            fg="white",
            bd=0,
            insertbackground="white",
            show="●",
        )
        self.entry_pass.place(x=360, y=160, width=250, height=25)

        btn_style = {
            "font": ("Segoe UI", 9, "bold"),
            "bd": 0,
            "cursor": "hand2",
            "fg": "#11111b",
        }

        self.btn_connecter = Button(
            self,
            text="Connecter",
            bg="#a6e3a1",
            command=self.tenter_connexion,
            **btn_style,
        )
        self.btn_connecter.place(x=360, y=210, width=120, height=35)
        self.btn_annuler = Button(
            self,
            text="Annuler",
            bg="#f38ba8",
            **btn_style,
            command=self.reset_fields,
        )
        self.btn_annuler.place(x=490, y=210, width=120, height=35)
        self.btn_quitter = Button(
            self,
            text="✖ Quitter",
            font=("Segoe UI", 10, "bold"),
            bg="#45475a",
            fg="#f38ba8",
            bd=0,
            cursor="hand2",
            command=lambda: sys.exit(),
        )
        self.btn_quitter.place(relx=0.5, y=300, anchor=CENTER, width=300, height=35)

    def tenter_connexion(self):
        user = self.entry_user.get()
        password = self.entry_pass.get()
        if not (user == "admin" and password == "1234"):
            messagebox.showerror("Erreur", "Identifiant de connexion incorrect")
            return
        self.seconnecter()

    def seconnecter(self):
        print("connexion reussi ... ")

    def reset_fields(self):
        self.entry_user.delete(0, tk.END)
        self.entry_pass.delete(0, tk.END)
