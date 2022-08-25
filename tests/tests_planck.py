from planck import Planck
import pytest


def test_energy_density():
    assert Planck.energy_density(10E-6, 213) == pytest.approx(5.824E-2, rel=1E-3)


@pytest.mark.parametrize(
    "wavelength, classification",
    (
        (380E-9, ("Visible", "Violet")),
        (450E-9, ("Visible", "Blue")),
        (485E-9, ("Visible", "Cyan")),
        (500E-9, ("Visible", "Green")),
        (565E-9, ("Visible", "Yellow")),
        (590E-9, ("Visible", "Orange")),
        (625E-9, ("Visible", "Red")),
    )
)
def test_spectral_categories(wavelength, classification):
    assert classification in Planck.spectral_categories(wavelength)
