import database
from tkinter import messagebox

# 1. RÉCUPÉRER TOUS LES ÉLÈVES 
def recuperer_tous_les_eleves():
    db = database.connecter()
    if db:
        cursor = db.cursor()
        # On récupère tout
        cursor.execute("SELECT * FROM eleve")
        resultat = cursor.fetchall()
        db.close()
        return resultat
    return []

# 2. AJOUTER UN ÉLÈVE
def ajouter_eleve(nom, prenom, d_naiss, email, tel, adr, classe, mat, cycle, sit_fin):
    db = database.connecter()
    if db:
        try:
            cursor = db.cursor()
         
            sql = """INSERT INTO eleve 
                     (nom, prenom, date_naissance, email, telephone, adresse, classe, matricule, cycle, situation_financiere) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            valeurs = (nom, prenom, d_naiss, email, tel, adr, classe, mat, cycle, sit_fin)
            cursor.execute(sql, valeurs)
            db.commit()
            messagebox.showinfo("Succès", f"L'étudiant {nom} a été ajouté !")
            return True
        except Exception as e:
            messagebox.showerror("Erreur SQL", f"Erreur lors de l'ajout : {e}")
            return False
        finally:
            db.close()

# 3. RECHERCHE FILTRÉE 
def rechercher_filtrer(critere, valeur):
    db = database.connecter()
    if db:
        cursor = db.cursor()
    
        colonne = "matricule" if critere == "Matricule" else "nom"
        
        # LIKE %valeur% permet de trouver même si on ne tape qu'une partie du nom
        query = f"SELECT matricule, nom, prenom, classe, cycle, telephone FROM eleves WHERE {colonne} LIKE %s"
        cursor.execute(query, (f"%{valeur}%",))
        
        resultats = cursor.fetchall()
        db.close()
        return resultats
    return []

# 4. RÉCUPÉRER UN ÉLÈVE PAR SON MATRICULE (Pour les détails ou modifs)
def rechercher_eleve(matricule):
    db = database.connecter()
    if db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM eleve WHERE matricule = %s", (matricule,))
        resultat = cursor.fetchone()
        db.close()
        return resultat
    return None

# 5. MODIFIER UN ÉLÈVE
def modifier_eleve(nom, prenom, d_naiss, email, tel, adr, classe, mat, cycle, sit_fin):
    db = database.connecter()
    if db:
        try:
            cursor = db.cursor()
            sql = """UPDATE eleve SET 
                     nom=%s, prenom=%s, date_naissance=%s, email=%s, telephone=%s, 
                     adresse=%s, classe=%s, cycle=%s, situation_financiere=%s 
                     WHERE matricule=%s"""
            valeurs = (nom, prenom, d_naiss, email, tel, adr, classe, cycle, sit_fin, mat)
            cursor.execute(sql, valeurs)
            db.commit()
            messagebox.showinfo("Succès", "Mise à jour effectuée !")
            return True
        except Exception as e:
            messagebox.showerror("Erreur", f"Echec de la modif : {e}")
            return False
        finally:
            db.close()