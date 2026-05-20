from models import Eleve
from datetime import date, datetime

eleve1 = Eleve(
    id=1,
    nom="Moukala",
    prenom="Jean-Pierre",
    date_naissance=date(2005, 3, 15),
    email="jp.moukala@ecole.cg",
    adresse="12 Rue de la Paix, Pointe-Noire",
    classe="Terminale A",
    telephone="06 123 45 67",
    date_inscription=datetime(2025, 9, 1, 8, 0, 0),
    matricule="MAT-2025-001",
)

eleve2 = Eleve(
    id=2,
    nom="Loemba",
    prenom="Grâce",
    date_naissance=date(2006, 7, 22),
    email="grace.loemba@ecole.cg",
    adresse="45 Avenue Lumumba, Brazzaville",
    classe="Première S",
    telephone="06 234 56 78",
    date_inscription=datetime(2025, 9, 1, 8, 30, 0),
    matricule="MAT-2025-002",
)

eleve3 = Eleve(
    id=3,
    nom="Nkodia",
    prenom="Christophe",
    date_naissance=date(2005, 11, 8),
    email="c.nkodia@ecole.cg",
    adresse="78 Boulevard Lyautey, Pointe-Noire",
    classe="Terminale S",
    telephone="05 345 67 89",
    date_inscription=datetime(2025, 9, 2, 9, 0, 0),
    matricule="MAT-2025-003",
)
