from view import ConnexionEcran
from service import AuthService


class ControllerConnexion:
    def __init__(self, view: ConnexionEcran, service: AuthService = None):
        self.view = view
        self.service = service

    def gerer_connexion(self):
        password, user = self.view.recupere_entree()
        if not (user == "admin" and password == "1234"):
            self.view.affiche_erreur("Erreur", "Identifiant de connexion incorrect")