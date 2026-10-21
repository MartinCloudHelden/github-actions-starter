"""Berechnet Versandkosten und Gesamtpreis eines Einkaufs."""

from decimal import Decimal


VERSANDPAUSCHALE = Decimal("4.90")
VERSANDFREI_AB = Decimal("50.00")


def versandkosten(warenwert: Decimal) -> Decimal:
    """Liefert die Versandkosten für einen nicht negativen Warenwert."""
    if warenwert < 0:
        raise ValueError("Der Warenwert darf nicht negativ sein.")

    if warenwert >= VERSANDFREI_AB:
        return Decimal("0.00")
    return VERSANDPAUSCHALE


def gesamtpreis(warenwert: Decimal) -> Decimal:
    """Liefert Warenwert plus Versandkosten."""
    return warenwert + versandkosten(warenwert)


if __name__ == "__main__":
    beispiel = Decimal("50.00")
    print(f"Warenwert: {beispiel:.2f} EUR")
    print(f"Gesamtpreis: {gesamtpreis(beispiel):.2f} EUR")

