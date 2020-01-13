import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k, pi


def planck(wavelengths, temperature):
    rho = (8 * pi * h * c) / (wavelengths**5 *
                              (np.exp((h * c) / (wavelengths * k * temperature)) - 1))
    return rho
