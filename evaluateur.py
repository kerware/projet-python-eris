# evaluateur.py

class NotAnIntegerError(Exception):
    """Exception levée quand la chaîne ne représente pas un entier valide."""
    pass


class GradeOutOfRangeError(Exception):
    """Exception levée quand la note entière est en dehors des bornes autorisées."""
    pass


def _parse_int_in_range(value_str: str, minimum: int, maximum: int, label: str) -> int:
    """
    Convertit une chaîne en entier et vérifie les bornes.
    :param value_str: chaîne représentant un entier
    :param minimum: valeur minimale autorisée
    :param maximum: valeur maximale autorisée
    :param label: libellé utilisé pour les messages d'erreur
    :return: entier valide dans les bornes
    :raises NotAnIntegerError: si la chaîne ne peut pas être convertie en entier
    :raises GradeOutOfRangeError: si l'entier est hors bornes
    """
    try:
        value = int(value_str)
    except ValueError:
        raise NotAnIntegerError(f"{label} doit être un entier valide : '{value_str}'")

    if value < minimum or value > maximum:
        raise GradeOutOfRangeError(
            f"{label} doit être comprise entre {minimum} et {maximum} (valeur reçue : {value})"
        )

    return value


def evaluer_etudiant(note_cours_str: str, note_examen_str: str) -> tuple[int, str]:
    """
    Prend en entrée deux chaînes représentant la note de cours et la note d'examen,
    vérifie leur validité, calcule la somme et renvoie (somme, niveau).

    Règles de niveau :
      - somme < 30  → D
      - somme < 50  → C
      - somme < 70  → B
      - sinon       → A

    :param note_cours_str: chaîne pour la note de cours (0 à 25)
    :param note_examen_str: chaîne pour la note d'examen (0 à 75)
    :return: (somme, niveau) où niveau ∈ {A, B, C, D}
    :raises NotAnIntegerError
    :raises GradeOutOfRangeError
    """
    note_cours = _parse_int_in_range(note_cours_str, 0, 25, "Note de cours")
    note_examen = _parse_int_in_range(note_examen_str, 0, 75, "Note d'examen")

    total = note_cours + note_examen

    if total < 30:
        niveau = "D"
    elif total < 50:
        niveau = "C"
    elif total < 70:
        niveau = "B"
    else:
        niveau = "A"

    return total, niveau
