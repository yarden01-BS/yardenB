import customtkinter as ctk
from tkinter import ttk

#configuration

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class GestionEleves(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Système de Gestion des Élèves - GESTIONDR1")
        self.geometry("1100x700")

        # --- Variables ---
        self.var_matricule = ctk.StringVar()
        self.var_nom = ctk.StringVar()
        self.var_prenom = ctk.StringVar()
        self.var_classe = ctk.StringVar()
        self.var_cycle = ctk.StringVar()
        self.var_sexe = ctk.StringVar(value="Masculin")
        self.var_situation = ctk.StringVar(value="0") # Mois soldés

        
        self.lbl_titre = ctk.CTkLabel(self, text="TABLEAU DE GESTION", 
                                      font=ctk.CTkFont(size=24, weight="bold"))
        self.lbl_titre.pack(pady=20)

     
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Les infos du formulaires 
        self.form_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.form_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        fields = [
            ("MATRICULE :", self.var_matricule),
            ("NOM :", self.var_nom),
            ("PRÉNOM :", self.var_prenom),
            ("CLASSE :", self.var_classe),
            ("ADRESSE :", None),
            ("EMAIL :", None),
            ("TÉLÉPHONE :", None),
            ("CYCLE :", self.var_cycle)
        ]

        for i, (text, var) in enumerate(fields):
            ctk.CTkLabel(self.form_frame, text=text, font=ctk.CTkFont(weight="bold")).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = ctk.CTkEntry(self.form_frame, width=250, textvariable=var)
            entry.grid(row=i, column=1, padx=10, pady=5)

        # La liste deroulante pour le sexe 
        ctk.CTkLabel(self.form_frame, text="SEXE :", font=ctk.CTkFont(weight="bold")).grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.combo_sexe = ctk.CTkComboBox(self.form_frame, values=["Masculin", "Féminin"], variable=self.var_sexe, width=250)
        self.combo_sexe.grid(row=8, column=1, padx=10, pady=5)

        # la situation fiancière, j'ai supposé que le nombre de mois est de 9
        ctk.CTkLabel(self.form_frame, text="SITUATION (Mois/9) :", font=ctk.CTkFont(weight="bold")).grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.slider_fin = ctk.CTkSegmentedButton(self.form_frame, values=["0","1","2","3","4","5","6","7","8","9"], variable=self.var_situation)
        self.slider_fin.grid(row=9, column=1, padx=10, pady=5)

        # Les boutons 
        self.btn_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.btn_frame.grid(row=0, column=1, padx=20, pady=20, sticky="n")

        # le bouton rechercher, la recherche se fait via le matricule 
        self.search_entry = ctk.CTkEntry(self.btn_frame, placeholder_text="Matricule...")
        self.search_entry.pack(pady=5, fill="x")
        ctk.CTkButton(self.btn_frame, text="Recherche", fg_color="#89b4fa", text_color="#1e1e2e").pack(pady=5, fill="x")

        # Les acition du CRUD, je les ai mise ensemble 
        actions = [("Ajouter", "#a6e3a1"), ("Modifier", "#f9e2af"), ("Supprimer", "#f38ba8"), 
                   ("Afficher", "#b4befe"), ("Annuler", "#6c7086"), ("RETOUR", "#45475a")]
        
        for text, color in actions:
            btn = ctk.CTkButton(self.btn_frame, text=text, fg_color=color, text_color="#11111b", font=ctk.CTkFont(weight="bold"))
            btn.pack(pady=5, fill="x")

        #La zonne inférieure 
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(padx=20, pady=20, fill="both", expand=True)

        columns = ("id", "nom", "prenom", "classe", "sexe", "cycle", "finances")
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings")

        # là, j'ai défini les entêtes 
        header_names = ["MATRICULE", "NOM", "PRÉNOM", "CLASSE", "SEXE", "CYCLE", "SOLDE (/9)"]
        for col, name in zip(columns, header_names):
            self.tree.heading(col, text=name)
            self.tree.column(col, width=100, anchor="center")

        # zt ici l style du tableau . 
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#2b2b3b", foreground="white", fieldbackground="#2b2b3b", rowheight=30)
        style.map("Treeview", background=[('selected', '#89b4fa')])

        self.tree.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = GestionEleves()
    app.mainloop()