from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Eleve:
    id: int
    nom: str
    prenom: str
    date_naissance: date
    email: str
    adresse: str
    classe: str
    telephone: str
    date_inscription: datetime
    matricule: str
