"""Geschäftsregeln für die Versandkosten. Diese Tests sind bereits fertig."""

from decimal import Decimal

import pytest

from shop.versand import gesamtpreis, versandkosten


@pytest.mark.parametrize(
    ("warenwert", "erwartet"),
    [
        ("0.00", "4.90"),
        ("49.99", "4.90"),
        ("50.00", "0.00"),
        ("50.01", "0.00"),
    ],
)
def test_versandkosten(warenwert: str, erwartet: str) -> None:
    assert versandkosten(Decimal(warenwert)) == Decimal(erwartet)


def test_gesamtpreis_unter_der_grenze() -> None:
    assert gesamtpreis(Decimal("10.00")) == Decimal("14.90")


def test_negativer_warenwert_wird_abgewiesen() -> None:
    with pytest.raises(ValueError):
        versandkosten(Decimal("-0.01"))

