from tkinter import *
from tkinter import ttk, messagebox

# NB: j'ai commenté  pour te faciliter la tache en cas de modification
# Les fonctions qui dynamisent les boutons


# Ici, pour l'ouverture de l'interface 2
def ouvrir_gestion():
    # Création d'une nouvelle fenêtre
    gestion = Toplevel()
    gestion.title("GESTIONDR1 - Enregistrement des Élèves")
    gestion.geometry("1100x750")
    gestion.configure(bg="#1e1e2e")

    Label(
        gestion,
        text="ENREGISTREMENT DES ÉLÈVES",
        font=("Segoe UI", 20, "bold"),
        bg="#1e1e2e",
        fg="#89b4fa",
    ).pack(pady=20)

    main_frame = Frame(gestion, bg="#2b2b3b", bd=1, relief=FLAT)
    main_frame.pack(padx=20, pady=10, fill="both", expand=True)

    # Colonne Gauche
    form_frame = Frame(main_frame, bg="#2b2b3b")
    form_frame.place(x=20, y=20)

    champs = [
        "MATRICULE :",
        "NOM :",
        "PRÉNOM :",
        "CLASSE :",
        "ADRESSE :",
        "EMAIL :",
        "TÉLÉPHONE :",
        "CYCLE :",
    ]
    for i, texte in enumerate(champs):
        Label(
            form_frame,
            text=texte,
            font=("Segoe UI", 10, "bold"),
            bg="#2b2b3b",
            fg="#89b4fa",
        ).grid(row=i, column=0, pady=8, sticky="w")
        Entry(form_frame, font=("Segoe UI", 11), bg="#313244", fg="white", bd=0).grid(
            row=i, column=1, padx=10, pady=8
        )

    # Le sexe
    Label(
        form_frame,
        text="SEXE :",
        font=("Segoe UI", 10, "bold"),
        bg="#2b2b3b",
        fg="#89b4fa",
    ).grid(row=8, column=0, pady=8, sticky="w")
    var_sexe = StringVar(value="Masculin")
    OptionMenu(form_frame, var_sexe, "Masculin", "Féminin").grid(
        row=8, column=1, padx=10, pady=8, sticky="ew"
    )

    # La situation
    Label(
        form_frame,
        text="SITUATION (/9 mois) :",
        font=("Segoe UI", 10, "bold"),
        bg="#2b2b3b",
        fg="#89b4fa",
    ).grid(row=9, column=0, pady=8, sticky="w")
    Entry(form_frame, font=("Segoe UI", 11), bg="#313244", fg="white", width=5).grid(
        row=9, column=1, padx=10, pady=8, sticky="w"
    )

    # Colonne Droite , les boutons
    btn_frame = Frame(main_frame, bg="#2b2b3b")
    btn_frame.place(x=450, y=20)

    #  le boutton de Recherche
    Entry(btn_frame, font=("Segoe UI", 11), bg="#313244", fg="white").pack(pady=5)
    Button(
        btn_frame,
        text="Recherche Matricule",
        bg="#89b4fa",
        font=("Segoe UI", 9, "bold"),
    ).pack(fill="x", pady=5)

    for txt, col in [
        ("Ajouter", "#a6e3a1"),
        ("Modifier", "#f9e2af"),
        ("Supprimer", "#f38ba8"),
        ("Afficher", "#b4befe"),
        ("Annuler", "#6c7086"),
        ("RETOUR", "#45475a"),
    ]:
        Button(btn_frame, text=txt, bg=col, font=("Segoe UI", 9, "bold"), bd=0).pack(
            fill="x", pady=5, ipady=5
        )

    # Le Tableau (Bas)
    table_frame = Frame(main_frame, bg="white")
    table_frame.place(x=20, y=450, width=1020, height=200)

    cols = ("ID", "Nom", "Prénom", "Classe", "Sexe", "Cycle", "Solde")
    tree = ttk.Treeview(table_frame, columns=cols, show="headings")
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=140)
    tree.pack(fill="both", expand=True)


# fonction de connexion
def tenter_connexion():
    user = entry_user.get()
    pw = entry_pass.get()

    # On vérifie les accès (ex: Admin / 1234)
    if user == "Admin" and pw == "1234":
        fenetre.withdraw()  # Cache la fenêtre de connexion
        ouvrir_gestion()  # Lance la page de gestion
    else:
        messagebox.showerror(
            "Erreur", "Identifiants incorrects\n(Utilisez Admin / 1234)"
        )


