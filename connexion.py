import tkinter as tk
from tkinter import messagebox
import os
import sys

# Gestion de l'import dynamique du fichier fonctions
try:
    import fonctions
except ImportError:
    try:
        import fonction as fonctions
    except ImportError:
        fonctions = None

def survol_entree(event):
    event.widget.config(bg="#f9e2af") 

def survol_sortie(event):
    if event.widget == btn_connecter:
        event.widget.config(bg="#a6e3a1")
    else:
        event.widget.config(bg="#f38ba8")

def tenter_connexion():
    user = entry_user.get()
    pw = entry_pass.get()
    
    # Vérification sécurisée
    if user == "Admin" and pw == "1234":
        fenetre.destroy()
        # Appel de l'interface moderne de gestion.py
        try:
            import gestion
            app = gestion.GestionEleves()
            app.mainloop()
        except Exception as e:
            messagebox.showerror("Erreur de lancement", f"Impossible d'ouvrir gestion.py : {e}")
    else:
        messagebox.showerror("Erreur", "Identifiants incorrects\n(Admin / 1234)")

# --- INTERFACE ---
fenetre = tk.Tk()
fenetre.geometry('750x550')
fenetre.title('Connexion Sécurisée - GESTIONDR1')
fenetre.configure(bg='#1e1e2e')

# Carte centrale
main_card = tk.Frame(fenetre, bg='#2b2b3b', bd=0, highlightthickness=1, highlightbackground="#45475a")
main_card.place(relx=0.5, rely=0.5, anchor="center", width=600, height=350)

tk.Label(main_card, text="CONNEXION", font=("Segoe UI", 18, "bold"), 
         bg='#2b2b3b', fg='#89b4fa').pack(pady=20)

# Champ Utilisateur
tk.Label(main_card, text="Utilisateur :", font=("Segoe UI", 10, "bold"), 
         bg='#2b2b3b', fg='#89b4fa').place(x=250, y=80)
entry_user = tk.Entry(main_card, font=("Segoe UI", 11), bg='#313244', fg="white", bd=0)
entry_user.place(x=250, y=110, width=300, height=30)

# Champ Mot de passe
tk.Label(main_card, text="Mot de passe :", font=("Segoe UI", 10, "bold"), 
         bg='#2b2b3b', fg='#89b4fa').place(x=250, y=160)
entry_pass = tk.Entry(main_card, font=("Segoe UI", 11), bg='#313244', fg="white", bd=0, show="●")
entry_pass.place(x=250, y=190, width=300, height=30)

# Boutons
btn_connecter = tk.Button(main_card, text="Connecter", bg="#a6e3a1", fg="#11111b", 
                          font=("Segoe UI", 10, "bold"), bd=0, command=tenter_connexion, cursor="hand2")
btn_connecter.place(x=250, y=250, width=140, height=40)

btn_annuler = tk.Button(main_card, text="Annuler", bg="#f38ba8", fg="#11111b", 
                        font=("Segoe UI", 10, "bold"), bd=0, command=lambda: [entry_user.delete(0,'end'), entry_pass.delete(0,'end')], cursor="hand2")
btn_annuler.place(x=410, y=250, width=140, height=40)

# Photo de profil (Cercle bleu)
canvas = tk.Canvas(main_card, width=150, height=150, bg="#2b2b3b", highlightthickness=0)
canvas.place(x=40, y=80)
canvas.create_oval(10, 10, 140, 140, fill="#89b4fa", outline="")

# Bindings survol
btn_connecter.bind("<Enter>", survol_entree)
btn_connecter.bind("<Leave>", survol_sortie)
btn_annuler.bind("<Enter>", survol_entree)
btn_annuler.bind("<Leave>", survol_sortie)

fenetre.mainloop()