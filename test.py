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


# ─────────────────────────────────────────
# 2. AFFICHER tous les élèves
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("TEST 2 — Affichage de tous les élèves")
print("=" * 50)

tous = service.afficher_eleves()
if tous:
    for e in tous:
        print(f"  {e}")
else:
    print("  ⚠️  Aucun élève trouvé.")


# ─────────────────────────────────────────
# 3. RECHERCHER par nom
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("TEST 3 — Recherche par nom : 'Mbemba'")
print("=" * 50)

resultats = service.rechercher_par_nom("Mbemba")
if resultats:
    for e in resultats:
        print(f"  ✅ Trouvé : {e}")
else:
    print("  ⚠️  Aucun élève trouvé avec ce nom.")


# ─────────────────────────────────────────
# 4. RECHERCHER par matricule
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("TEST 4 — Recherche par matricule : 'MAT-2024-002'")
print("=" * 50)

eleve_trouve = service.rechercher_par_matricule("MAT-2024-002")
if eleve_trouve:
    print(f"  ✅ Trouvé : {eleve_trouve}")
else:
    print("  ⚠️  Aucun élève trouvé avec ce matricule.")


# ─────────────────────────────────────────
# 5. MODIFIER un élève (on récupère l'id via le matricule)
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("TEST 5 — Modification de l'élève MAT-2024-001")
print("=" * 50)

eleve_existant = service.rechercher_par_matricule("MAT-2024-001")
if eleve_existant:
    eleve_id = eleve_existant[0]  # l'id est généralement la 1ère colonne
    eleve_modifie = Eleve(
        nom="Mbemba", prenom="Jean-Pierre",       # prénom modifié
        date_naissance="2005-03-15",
        email="jeanpierre.mbemba@email.com",       # email modifié
        telephone="06 12 34 56 78",
        adresse="12 Rue de la Paix, Brazzaville",
        classe="Terminale S", matricule="MAT-2024-001",
        situation_financiere="Sans bourse",        # situation modifiée
        cycle=Cycle.LYCEE
    )
    service.modifier_eleve(eleve_id, eleve_modifie)
    print(f"  ✅ Élève {eleve_id} modifié avec succès.")
else:
    print("  ⚠️  Élève introuvable, modification annulée.")


# ─────────────────────────────────────────
# 6. VÉRIFIER la modification
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("TEST 6 — Vérification après modification")
print("=" * 50)

verification = service.rechercher_par_matricule("MAT-2024-001")
print(f"  Résultat : {verification}")


# ─────────────────────────────────────────
# 7. SUPPRIMER un élève
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("TEST 7 — Suppression de l'élève MAT-2024-003")
print("=" * 50)

eleve_a_supprimer = service.rechercher_par_matricule("MAT-2024-003")
if eleve_a_supprimer:
    eleve_id = eleve_a_supprimer[0]
    service.supprimer_eleve(eleve_id)
    print(f"  ✅ Élève {eleve_id} supprimé avec succès.")
else:
    print("  ⚠️  Élève introuvable, suppression annulée.")


# ─────────────────────────────────────────
# 8. VÉRIFIER la suppression
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("TEST 8 — Vérification après suppression")
print("=" * 50)

verification = service.rechercher_par_matricule("MAT-2024-003")
if not verification:
    print("  ✅ Suppression confirmée, élève introuvable.")
else:
    print(f"  ⚠️  L'élève existe encore : {verification}")


# ─────────────────────────────────────────
# 9. ÉTAT FINAL de la base
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("TEST 9 — État final de la base")
print("=" * 50)

final = service.afficher_eleves()
print(f"  Nombre d'élèves en base : {len(final)}")
for e in final:
    print(f"  {e}")

print("\n✅ Tous les tests sont terminés.")