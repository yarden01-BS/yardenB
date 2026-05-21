import customtkinter as ctk
from tkinter import ttk, messagebox

# --- DONNÉES FICTIVES POUR APPARENCE DE L'UI ---
MOCK_DATA = [
    ("MAT001", "KOUBA", "Nathan", "Terminale C", "Masculin", "Lycée", "En règle"),
    ("MAT002", "MBOUSSA", "Grace", "Première S", "Féminin", "Lycée", "6/9 mois"),
    ("MAT003", "NTSOUMOU", "Arnaud", "3ème A", "Masculin", "Collège", "En règle"),
]


class GestionElevesFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="#1e1e2e")

        # Variables d'état de l'interface
        self.var_mat = ctk.StringVar()
        self.var_nom = ctk.StringVar()
        self.var_pre = ctk.StringVar()
        self.var_cla = ctk.StringVar()
        self.var_adr = ctk.StringVar()
        self.var_mail = ctk.StringVar()
        self.var_tel = ctk.StringVar()
        self.var_cyc = ctk.StringVar(value="Lycée")
        self.var_naiss = ctk.StringVar()
        self.var_insc = ctk.StringVar()
        self.var_sex = ctk.StringVar(value="Masculin")
        self.var_sit = ctk.StringVar()

        self.var_recherche = ctk.StringVar()
        self.filtre_recherche = ctk.StringVar(value="Matricule")

        self.pack(fill="both", expand=True)

        # --- TITRE ---
        ctk.CTkLabel(
            self,
            text="ENREGISTREMENT DES ÉLÈVES",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#89b4fa",
        ).pack(pady=20)

        # --- ZONE FORMULAIRE ---
        self.form_frame = ctk.CTkFrame(self, fg_color="#2b2b3b", corner_radius=15)
        self.form_frame.pack(padx=20, pady=10, fill="x")

        # Ligne 0 : Matricule, Nom
        ctk.CTkLabel(
            self.form_frame, text="MATRICULE :", font=("Arial", 11, "bold")
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkEntry(self.form_frame, textvariable=self.var_mat, width=180).grid(
            row=0, column=1, padx=10, pady=10
        )

        ctk.CTkLabel(self.form_frame, text="NOM :", font=("Arial", 11, "bold")).grid(
            row=0, column=2, padx=10, pady=10, sticky="w"
        )
        ctk.CTkEntry(self.form_frame, textvariable=self.var_nom, width=180).grid(
            row=0, column=3, padx=10, pady=10
        )

        # --- BLOC RECHERCHE RE-DISPOSÉ (AVEC LES COULEURS D'ORIGINE) ---
        recherche_frame = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        recherche_frame.grid(row=0, column=4, padx=30, pady=10, sticky="nsew")

        # Ligne du haut : Recherche à gauche, Filtre à droite
        recherche_input_frame = ctk.CTkFrame(recherche_frame, fg_color="transparent")
        recherche_input_frame.pack(side="top", fill="x", pady=(0, 5))

        ctk.CTkEntry(
            recherche_input_frame,
            placeholder_text="Rechercher...",
            textvariable=self.var_recherche,
            width=150,
        ).pack(side="left", padx=(0, 5))

        ctk.CTkComboBox(
            recherche_input_frame,
            values=["Matricule", "Nom"],
            variable=self.filtre_recherche,
            width=110,
        ).pack(side="left")

        # Bouton en bas : Pleine largeur avec le bleu ciel d'origine
        ctk.CTkButton(
            recherche_frame,
            text="OK",
            command=self.rechercher,
            fg_color="#89b4fa",
            text_color="black",
            font=("Arial", 12, "bold"),
        ).pack(side="top", fill="x")
        # ---------------------------------------------------------------

        # Ligne 1 : Prénom, Classe
        ctk.CTkLabel(self.form_frame, text="PRÉNOM :", font=("Arial", 11, "bold")).grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )
        ctk.CTkEntry(self.form_frame, textvariable=self.var_pre, width=180).grid(
            row=1, column=1, padx=10, pady=10
        )
        ctk.CTkLabel(self.form_frame, text="CLASSE :", font=("Arial", 11, "bold")).grid(
            row=1, column=2, padx=10, pady=10, sticky="w"
        )
        ctk.CTkEntry(self.form_frame, textvariable=self.var_cla, width=180).grid(
            row=1, column=3, padx=10, pady=10
        )

        # Ligne 2 : Adresse, Email
        ctk.CTkLabel(
            self.form_frame, text="ADRESSE :", font=("Arial", 11, "bold")
        ).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkEntry(self.form_frame, textvariable=self.var_adr, width=180).grid(
            row=2, column=1, padx=10, pady=10
        )
        ctk.CTkLabel(self.form_frame, text="EMAIL :", font=("Arial", 11, "bold")).grid(
            row=2, column=2, padx=10, pady=10, sticky="w"
        )
        ctk.CTkEntry(self.form_frame, textvariable=self.var_mail, width=180).grid(
            row=2, column=3, padx=10, pady=10
        )

        # Ligne 3 : Téléphone, Cycle
        ctk.CTkLabel(
            self.form_frame, text="TÉLÉPHONE :", font=("Arial", 11, "bold")
        ).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkEntry(self.form_frame, textvariable=self.var_tel, width=180).grid(
            row=3, column=1, padx=10, pady=10
        )
        ctk.CTkLabel(self.form_frame, text="CYCLE :", font=("Arial", 11, "bold")).grid(
            row=3, column=2, padx=10, pady=10, sticky="w"
        )
        ctk.CTkComboBox(
            self.form_frame,
            values=["Primaire", "Collège", "Lycée", "Université"],
            variable=self.var_cyc,
            width=180,
        ).grid(row=3, column=3, padx=10, pady=10)

        # Ligne 4 : Sexe, Situation
        ctk.CTkLabel(self.form_frame, text="SEXE :", font=("Arial", 11, "bold")).grid(
            row=4, column=0, padx=10, pady=10, sticky="w"
        )
        ctk.CTkComboBox(
            self.form_frame,
            values=["Masculin", "Féminin"],
            variable=self.var_sex,
            width=180,
        ).grid(row=4, column=1, padx=10, pady=10)
        ctk.CTkLabel(
            self.form_frame, text="SITUATION :", font=("Arial", 11, "bold")
        ).grid(row=4, column=2, padx=10, pady=10, sticky="w")
        ctk.CTkEntry(
            self.form_frame,
            textvariable=self.var_sit,
            width=180,
            placeholder_text="/9 mois",
        ).grid(row=4, column=3, padx=10, pady=10)

        # --- ACTIONS (BOUTONS) ---
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=15)

        # C'est beaucoup plus parlant à la lecture
        boutons = [
            {
                "text": "Ajouter",
                "color": "#a6e3a1",
                "command": self.ajouter,
                "text_color": "black",
            },
            {
                "text": "Modifier",
                "color": "#f9e2af",
                "command": self.modifier,
                "text_color": "black",
            },
            {
                "text": "Supprimer",
                "color": "#f38ba8",
                "command": self.supprimer,
                "text_color": "black",
            },
            {
                "text": "RETOUR",
                "color": "#45475a",
                "command": self.retour,
                "text_color": "white",
            },
            {
                "text": "Afficher",
                "color": "#b4befe",
                "command": self.afficher_details,
                "text_color": "black",
            },
            {
                "text": "Annuler",
                "color": "#6c7086",
                "command": self.reinitialiser,
                "text_color": "white",
            },
        ]

        for i, btn_config in enumerate(boutons):
            ctk.CTkButton(
                self.btn_frame,
                text=btn_config["text"],
                fg_color=btn_config["color"],
                text_color=btn_config["text_color"],
                width=110,
                font=("Arial", 12, "bold"),
                command=btn_config["command"],
            ).grid(row=0, column=i, padx=5)

        # --- TABLEAU DES DONNÉES (TREEVIEW) ---
        self.tree_frame = ctk.CTkFrame(self)
        self.tree_frame.pack(padx=20, pady=10, fill="both", expand=True)

        cols = ("id", "nom", "pre", "cla", "sex", "cyc", "sit")
        self.tree = ttk.Treeview(self.tree_frame, columns=cols, show="headings")

        for c, h in zip(
            cols,
            ["ID / MATRICULE", "NOM", "PRÉNOM", "CLASSE", "SEXE", "CYCLE", "SOLDE"],
        ):
            self.tree.heading(c, text=h)
            self.tree.column(c, width=120, anchor="center")

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<Double-1>", lambda e: self.remplir_champs())

        # Chargement initial visuel
        self.charger_donnees()

    # ================= COMPORTEMENTS COMPOSANTS (UI ONLY) =================

    def charger_donnees(self):
        for r in self.tree.get_children():
            self.tree.delete(r)
        for student in MOCK_DATA:
            self.tree.insert("", "end", values=student)

    def ajouter(self):
        if self.var_mat.get() and self.var_nom.get():
            nouvel_eleve = (
                self.var_mat.get(),
                self.var_nom.get(),
                self.var_pre.get(),
                self.var_cla.get(),
                self.var_sex.get(),
                self.var_cyc.get(),
                self.var_sit.get(),
            )
            self.tree.insert("", "end", values=nouvel_eleve)
            self.reinitialiser()
        else:
            messagebox.showwarning(
                "Champs requis",
                "Veuillez au moins renseigner le Matricule et le Nom pour tester l'ajout.",
            )

    def modifier(self):
        selected = self.tree.selection()
        if selected:
            self.tree.item(
                selected[0],
                values=(
                    self.var_mat.get(),
                    self.var_nom.get(),
                    self.var_pre.get(),
                    self.var_cla.get(),
                    self.var_sex.get(),
                    self.var_cyc.get(),
                    self.var_sit.get(),
                ),
            )

    def supprimer(self):
        selected = self.tree.selection()
        if selected:
            m = self.tree.item(selected[0])["values"][0]
            if messagebox.askyesno(
                "Confirmation UI", f"Supprimer visuellement l'élève {m} du tableau ?"
            ):
                self.tree.delete(selected[0])
                self.reinitialiser()

    def rechercher(self):
        critere = self.var_recherche.get().lower()
        for r in self.tree.get_children():
            self.tree.delete(r)

        for student in MOCK_DATA:
            idx = 0 if self.filtre_recherche.get() == "Matricule" else 1
            if critere in student[idx].lower():
                self.tree.insert("", "end", values=student)

    def remplir_champs(self):
        try:
            sel = self.tree.selection()[0]
            values = self.tree.item(sel)["values"]

            self.var_mat.set(values[0])
            self.var_nom.set(values[1])
            self.var_pre.set(values[2])
            self.var_cla.set(values[3])
            self.var_sex.set(values[4])
            self.var_cyc.set(values[5])
            self.var_sit.set(values[6])
        except IndexError:
            pass

    def afficher_details(self):
        if not self.var_mat.get():
            return

        w = ctk.CTkToplevel(self)
        w.geometry("400x400")
        w.title("Aperçu Détails UI")
        w.attributes("-topmost", True)

        ctk.CTkLabel(
            w,
            text="DÉTAILS ÉLÈVE (PREVIEW)",
            font=("Arial", 18, "bold"),
            text_color="#89b4fa",
        ).pack(pady=20)

        txt = (
            f"Matricule : {self.var_mat.get()}\n"
            f"Nom : {self.var_nom.get()}\n"
            f"Prénom : {self.var_pre.get()}\n"
            f"Classe : {self.var_cla.get()}\n"
            f"Cycle : {self.var_cyc.get()}\n"
            f"Solde/Situation : {self.var_sit.get()}"
        )

        ctk.CTkLabel(w, text=txt, font=("Arial", 13), justify="left").pack(
            pady=5, padx=20
        )

    def reinitialiser(self):
        for v in [
            self.var_mat,
            self.var_nom,
            self.var_pre,
            self.var_cla,
            self.var_adr,
            self.var_mail,
            self.var_tel,
            self.var_naiss,
            self.var_sit,
            self.var_recherche,
        ]:
            v.set("")

    def retour(self):
        print("Action Bouton Retour déclenchée")


# ================= ENVIRONNEMENT DE TEST EXEC =================

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("1200x800")
    app.title("Prototypage UI - Gestion Élèves")

    GestionElevesFrame(app)
    app.mainloop()
