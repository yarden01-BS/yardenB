from models import Eleve, Cycle
from services import EleveService

service = EleveService()

# ─────────────────────────────────────────
# 1. AJOUTER des élèves
# ─────────────────────────────────────────
print("=" * 50)
print("TEST 1 — Ajout d'élèves")
print("=" * 50)

eleves_a_ajouter = [
    Eleve(
        nom="Mbemba", prenom="Jean",
        date_naissance="2005-03-15",
        email="jean.mbemba@email.com",
        telephone="06 12 34 56 78",
        adresse="12 Rue de la Paix, Brazzaville",
        classe="Terminale S", matricule="MAT-2024-001",
        situation_financiere="Bourse complète",
        cycle=Cycle.LYCEE
    ),
    Eleve(
        nom="Nguesso", prenom="Marie",
        date_naissance="2008-07-22",
        email="marie.nguesso@email.com",
        telephone="06 98 76 54 32",
        adresse="45 Avenue Foch, Brazzaville",
        classe="6ème A", matricule="MAT-2024-002",
        situation_financiere="Demi-bourse",
        cycle=Cycle.COLLEGE
    ),
    Eleve(
        nom="Bakala", prenom="Sophie",
        date_naissance="2001-01-30",
        email="sophie.bakala@email.com",
        telephone="06 11 22 33 44",
        adresse="23 Rue Loubaki, Brazzaville",
        classe="Licence 2 Info", matricule="MAT-2024-003",
        situation_financiere="Bourse universitaire",
        cycle=Cycle.UNIVERSITE
    ),
]

for eleve in eleves_a_ajouter:
    service.ajouter_eleve(eleve)
    print(f"  ✅ Ajouté : {eleve.prenom} {eleve.nom} ({eleve.cycle.value})")


