from models import Eleve
from database import EleveDAO


class EleveService:
    def __init__(self):
        self.dao = EleveDAO()

    def _valider_texte(self, valeur: str, message: str):
        valeur = valeur.strip()

        if not valeur:
            raise ValueError(message)

        return valeur

    def afficher_eleves(self):
        return self.dao.rechercher_tous()

    def rechercher_par_nom(self, nom: str):
        nom = self._valider_texte(nom, "Nom invalide")
        return self.dao.rechercher_par_nom(nom)

    def rechercher_par_matricule(self, matricule: str):
        matricule = self._valider_texte(matricule, "Matricule invalide")
        return self.dao.rechercher_par_matricule(matricule)

    def ajouter_eleve(self, eleve: Eleve):
        eleve.nom = self._valider_texte(eleve.nom, "Le nom est obligatoire")

        eleve.matricule = self._valider_texte(
            eleve.matricule, "Le matricule est obligatoire"
        )

        if self.dao.rechercher_par_matricule(eleve.matricule):
            raise ValueError("Ce matricule existe déjà")

        self.dao.ajouter_eleve(eleve)

    def modifier_eleve(self, id: int, eleve: Eleve):
        if id <= 0:
            raise ValueError("ID invalide")
        eleve.nom = self._valider_texte(eleve.nom, "Le nom est obligatoire")
        eleve.matricule = self._valider_texte(
            eleve.matricule, "Le matricule est obligatoire"
        )
        ancien = self.dao.rechercher_par_matricule(eleve.matricule)
        if ancien and ancien.id != id:
            raise ValueError("Ce matricule est déjà utilisé")
        self.dao.modifier_eleve(id, eleve)

    def supprimer_eleve(self, id: int):
        if id <= 0:
            raise ValueError("ID invalide")

        self.dao.supprimer_eleve(id)
