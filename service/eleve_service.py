from models import Eleve
from database import EleveDAO


class EleveService:
    def __init__(self):
        self.dao = EleveDAO()

    def affiche_eleves(self):
        return self.dao.rechercher_tous()

    def recherche_par_nom(self, nom: str):
        return self.dao.rechercher_par_nom(nom)

    def ajouter_eleve(self, eleve: Eleve):
        self.dao.ajouter_eleve(eleve)

    def modifier_eleve(self, id: int, eleve: Eleve):
        self.dao.modifier_eleve(id, eleve)

    def supprimer_eleve(self, id: int):
        self.dao.supprimer_eleve(id)
