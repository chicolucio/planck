import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k, pi


def planck(wavelength, temperature):
    rho = (8 * pi * h * c) / (wavelength**5 * (np.exp((h * c) /
                                                      (wavelength * k *
                                                       temperature)) - 1))
    return rho
