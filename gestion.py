import customtkinter as ctk
from tkinter import ttk, messagebox
try:
    import fonctions
except ImportError:
    try:
        import fonction as fonctions
    except ImportError:
        fonctions = None

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class GestionEleves(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Système de Gestion Moderne - GESTIONDR1")
        self.geometry("1200x800")
        self.configure(fg_color="#1e1e2e")

        # Variables
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

        ctk.CTkLabel(self, text="ENREGISTREMENT DES ÉLÈVES", 
                     font=ctk.CTkFont(size=24, weight="bold"), text_color="#89b4fa").pack(pady=20)

        # --- ZONE FORMULAIRE ---
        self.form_frame = ctk.CTkFrame(self, fg_color="#2b2b3b", corner_radius=15)
        self.form_frame.pack(padx=20, pady=10, fill="x")

        # Ligne 0 : MATRICULE et NOM + RECHERCHE
        ctk.CTkLabel(self.form_frame, text="MATRICULE :", font=("Arial", 11, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkEntry(self.form_frame, textvariable=self.var_mat, width=180).grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkLabel(self.form_frame, text="NOM :", font=("Arial", 11, "bold")).grid(row=0, column=2, padx=10, pady=10, sticky="w")
        ctk.CTkEntry(self.form_frame, textvariable=self.var_nom, width=180).grid(row=0, column=3, padx=10, pady=10)

        # RECHERCHE HORIZONTALE
        recherche_frame = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        recherche_frame.grid(row=0, column=4, padx=30, pady=10)
        ctk.CTkComboBox(recherche_frame, values=["Matricule", "Nom"], variable=self.filtre_recherche, width=110).pack(side="left", padx=5)
        ctk.CTkEntry(recherche_frame, placeholder_text="Rechercher...", textvariable=self.var_recherche, width=150).pack(side="left", padx=5)
        ctk.CTkButton(recherche_frame, text="OK", width=50, command=self.rechercher, fg_color="#89b4fa", text_color="black").pack(side="left", padx=5)

        # Ligne 1 : PRÉNOM et CLASSE
        ctk.CTkLabel(self.form_frame, text="PRÉNOM :", font=("Arial", 11, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkEntry(self.form_frame, textvariable=self.var_pre, width=180).grid(row=1, column=1, padx=10, pady=10)
        ctk.CTkLabel(self.form_frame, text="CLASSE :", font=("Arial", 11, "bold")).grid(row=1, column=2, padx=10, pady=10, sticky="w")
        ctk.CTkEntry(self.form_frame, textvariable=self.var_cla, width=180).grid(row=1, column=3, padx=10, pady=10)

        # Ligne 2 : ADRESSE et EMAIL
        ctk.CTkLabel(self.form_frame, text="ADRESSE :", font=("Arial", 11, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkEntry(self.form_frame, textvariable=self.var_adr, width=180).grid(row=2, column=1, padx=10, pady=10)
        ctk.CTkLabel(self.form_frame, text="EMAIL :", font=("Arial", 11, "bold")).grid(row=2, column=2, padx=10, pady=10, sticky="w")
        ctk.CTkEntry(self.form_frame, textvariable=self.var_mail, width=180).grid(row=2, column=3, padx=10, pady=10)

        # Ligne 3 : TÉLÉPHONE et CYCLE
        ctk.CTkLabel(self.form_frame, text="TÉLÉPHONE :", font=("Arial", 11, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkEntry(self.form_frame, textvariable=self.var_tel, width=180).grid(row=3, column=1, padx=10, pady=10)
        ctk.CTkLabel(self.form_frame, text="CYCLE :", font=("Arial", 11, "bold")).grid(row=3, column=2, padx=10, pady=10, sticky="w")
        ctk.CTkComboBox(self.form_frame, values=["Primaire", "Collège", "Lycée", "Université"], variable=self.var_cyc, width=180).grid(row=3, column=3, padx=10, pady=10)

        # Ligne 4 : SEXE et SITUATION
        ctk.CTkLabel(self.form_frame, text="SEXE :", font=("Arial", 11, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkComboBox(self.form_frame, values=["Masculin", "Féminin"], variable=self.var_sex, width=180).grid(row=4, column=1, padx=10, pady=10)
        ctk.CTkLabel(self.form_frame, text="SITUATION :", font=("Arial", 11, "bold")).grid(row=4, column=2, padx=10, pady=10, sticky="w")
        ctk.CTkEntry(self.form_frame, textvariable=self.var_sit, width=180, placeholder_text="/9 mois").grid(row=4, column=3, padx=10, pady=10)

        # --- BOUTONS ---
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=15)

        boutons = [
            ("Ajouter", "#a6e3a1", self.ajouter), ("Modifier", "#f9e2af", self.modifier),
            ("Supprimer", "#f38ba8", self.supprimer), ("Afficher", "#b4befe", self.afficher_details),
            ("Annuler", "#6c7086", self.reinitialiser), ("RETOUR", "#45475a", self.retour)
        ]

        for i, (txt, col, cmd) in enumerate(boutons):
            ctk.CTkButton(self.btn_frame, text=txt, fg_color=col, text_color="black" if i<4 else "white", 
                          width=110, font=("Arial", 12, "bold"), command=cmd).grid(row=0, column=i, padx=5)

        # --- TABLEAU ---
        self.tree_frame = ctk.CTkFrame(self)
        self.tree_frame.pack(padx=20, pady=10, fill="both", expand=True)

        cols = ("id", "nom", "pre", "cla", "sex", "cyc", "sit")
        self.tree = ttk.Treeview(self.tree_frame, columns=cols, show="headings")
        for c, h in zip(cols, ["ID", "NOM", "PRÉNOM", "CLASSE", "SEXE", "CYCLE", "SOLDE"]):
            self.tree.heading(c, text=h)
            self.tree.column(c, width=120, anchor="center")
        
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<Double-1>", lambda e: self.remplir_champs())
        
        # On charge les données au démarrage
        self.charger_donnees()

    def charger_donnees(self):
        if fonctions:
            for r in self.tree.get_children(): self.tree.delete(r)
            # ICI : Ton fichier fonctions doit utiliser SELECT * FROM eleve (SANS S)
            data = fonctions.recuperer_tous_les_eleves()
            if data:
                for r in data: self.tree.insert("", "end", values=(r[0], r[1], r[2], r[7], r[12], r[10], r[11]))

    def ajouter(self):
        if fonctions and fonctions.ajouter_eleve(self.var_nom.get(), self.var_pre.get(), self.var_naiss.get(), self.var_mail.get(), self.var_tel.get(), self.var_adr.get(), self.var_cla.get(), self.var_mat.get(), self.var_cyc.get(), self.var_sit.get()):
            self.charger_donnees()
            self.reinitialiser()

    def modifier(self):
        if fonctions and fonctions.modifier_eleve(self.var_nom.get(), self.var_pre.get(), self.var_naiss.get(), self.var_mail.get(), self.var_tel.get(), self.var_adr.get(), self.var_cla.get(), self.var_mat.get(), self.var_cyc.get(), self.var_sit.get()):
            self.charger_donnees()

    def supprimer(self):
        m = self.var_mat.get()
        if m and messagebox.askyesno("Confirmation", f"Supprimer l'élève {m} ?"):
            # fonctions.supprimer_eleve(m) # À créer dans fonctions.py
            self.charger_donnees()

    def rechercher(self):
        if fonctions:
            res = fonctions.rechercher_filtrer(self.filtre_recherche.get(), self.var_recherche.get())
            for r in self.tree.get_children(): self.tree.delete(r)
            for i in res: self.tree.insert("", "end", values=i)

    def remplir_champs(self):
        try:
            sel = self.tree.selection()[0]
            m = self.tree.item(sel)['values'][0] # On prend l'ID ou le matricule
            e = fonctions.rechercher_eleve(m)
            if e:
                self.var_nom.set(e[1]); self.var_pre.set(e[2]); self.var_mat.set(e[9])
                self.var_cla.set(e[7]); self.var_cyc.set(e[10]); self.var_sit.set(e[11])
        except: pass

    def afficher_details(self):
        m = self.var_mat.get()
        if m and fonctions:
            e = fonctions.rechercher_eleve(m)
            if e:
                w = ctk.CTkToplevel(self); w.geometry("400x500"); w.title("Détails"); w.attributes("-topmost", True)
                ctk.CTkLabel(w, text="DÉTAILS ÉLÈVE", font=("Arial", 20, "bold"), text_color="#89b4fa").pack(pady=20)
                txt = f"Matricule: {e[9]}\nNom: {e[1]}\nPrénom: {e[2]}\nClasse: {e[7]}\nCycle: {e[10]}\nSituation: {e[11]}"
                ctk.CTkLabel(w, text=txt, font=("Arial", 13), justify="left").pack(pady=5, padx=20)

    def reinitialiser(self):
        for v in [self.var_mat, self.var_nom, self.var_pre, self.var_cla, self.var_adr, self.var_mail, self.var_tel, self.var_naiss, self.var_sit]: v.set("")

    def retour(self):
        self.destroy()
        import os
        os.system("python connexion.py")

if __name__ == "__main__":
    app = GestionEleves()
    app.mainloop()