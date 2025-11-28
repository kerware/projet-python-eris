# noqa: E501
# test_evaluateur.py

import pytest
from evaluateur import (
    evaluer_etudiant,
    NotAnIntegerError,
    GradeOutOfRangeError,
)


# --- Tests positifs paramétrés : cas aux limites des niveaux --- #
# On couvre les transitions :
#   - 29 -> D, 30 -> C
#   - 49 -> C, 50 -> B
#   - 69 -> B, 70 -> A

@pytest.mark.parametrize(
    "note_cours, note_examen, total_attendu, niveau_attendu",
    [
        ("25", "4", 29, "D"),   # frontière D (juste en dessous de 30)
        ("25", "5", 30, "C"),   # passage D -> C

        ("25", "24", 49, "C"),  # frontière C (juste en dessous de 50)
        ("25", "25", 50, "B"),  # passage C -> B

        ("25", "44", 69, "B"),  # frontière B (juste en dessous de 70)
        ("25", "45", 70, "A"),  # passage B -> A
    ],
)
def test_niveaux_aux_limites(note_cours, note_examen, total_attendu, niveau_attendu):
    total, niveau = evaluer_etudiant(note_cours, note_examen)
    assert total == total_attendu
    assert niveau == niveau_attendu


# --- Tests négatifs paramétrés : erreurs de format (NotAnIntegerError) --- #

@pytest.mark.parametrize(
    "note_cours, note_examen",
    [
        ("abc", "10"),   # note de cours non entière
        ("10", "xyz"),   # note d'examen non entière
        ("foo", "bar"),  # les deux sont non entiers
        ("", "10"),      # chaîne vide pour cours
        ("10", ""),      # chaîne vide pour examen
    ],
)
def test_notes_non_entieres(note_cours, note_examen):
    with pytest.raises(NotAnIntegerError):
        evaluer_etudiant(note_cours, note_examen)


# --- Tests négatifs paramétrés : erreurs de bornes (GradeOutOfRangeError) --- #

@pytest.mark.parametrize(
    "note_cours, note_examen",
    [
        ("26", "10"),   # note de cours trop grande (> 25)
        ("-1", "10"),   # note de cours négative
        ("10", "76"),   # note d'examen trop grande (> 75)
        ("10", "-1"),   # note d'examen négative
        ("30", "80"),   # les deux hors bornes
    ],
)
def test_notes_hors_bornes(note_cours, note_examen):
    with pytest.raises(GradeOutOfRangeError):
        evaluer_etudiant(note_cours, note_examen)
