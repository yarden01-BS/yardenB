from database import Database
from models import Eleve, Cycle


class EleveDAO:
    def __init__(self):
        self.database = Database()

    def rechercher_tous(self):
        with self.database as db:
            query = "SELECT * FROM eleve"
            db.cursor.execute(query)
            return db.cursor.fetchall()

    def rechercher_par_nom(self, nom: str):
        with self.database as db:
            query = "SELECT * FROM eleve WHERE nom = %s"
            db.cursor.execute(query, (nom,))
            return db.cursor.fetchall()

    def rechercher_par_matricule(self, matricule: str):
        with self.database as db:
            query = "SELECT * FROM eleve WHERE matricule = %s"
            db.cursor.execute(query, (matricule,))
            return db.cursor.fetchone()

    def rechercher_par_id(self, eleve_id: int):
        with self.database as db:
            query = "SELECT * FROM eleve WHERE id = %s"
            db.cursor.execute(query, (eleve_id,))
            return db.cursor.fetchone()

    def ajouter_eleve(self, eleve: Eleve):
        with self.database as db:
            query = (
                "INSERT INTO `eleve` "
                "(`nom`, `prenom`, `date_naissance`, `email`, `telephone`, `adresse`, `classe`, `matricule`, `situation_financiere`, `cycle`, `date_inscription`) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            )
            db.cursor.execute(
                query,
                (
                    eleve.nom,
                    eleve.prenom,
                    eleve.date_naissance,
                    eleve.email,
                    eleve.telephone,
                    eleve.adresse,
                    eleve.classe,
                    eleve.matricule,
                    eleve.situation_financiere,
                    (
                        eleve.cycle.value
                        if isinstance(eleve.cycle, Cycle)
                        else eleve.cycle
                    ),
                    eleve.date_inscription,
                ),
            )
            db.connection.commit()

    def modifier_eleve(self, eleve_id: int, eleve: Eleve):
        with self.database as db:
            query = (
                "UPDATE `eleve` SET "
                "`nom` = %s, `prenom` = %s, `date_naissance` = %s, `email` = %s, `telephone` = %s, "
                "`adresse` = %s, `classe` = %s, `matricule` = %s, `situation_financiere` = %s, `cycle` = %s "
                "WHERE id = %s"
            )
            db.cursor.execute(
                query,
                (
                    eleve.nom,
                    eleve.prenom,
                    eleve.date_naissance,
                    eleve.email,
                    eleve.telephone,
                    eleve.adresse,
                    eleve.classe,
                    eleve.matricule,
                    eleve.situation_financiere,
                    (
                        eleve.cycle.value
                        if isinstance(eleve.cycle, Cycle)
                        else eleve.cycle
                    ),
                    eleve_id,
                ),
            )
            db.connection.commit()

    def supprimer_eleve(self, eleve_id: int):
        with self.database as db:
            query = "DELETE FROM `eleve` WHERE id = %s"
            db.cursor.execute(query, (eleve_id,))
            db.connection.commit()
