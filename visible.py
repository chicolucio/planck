import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np


def wavelength_to_rgb(wavelength, gamma=0.8):
    """
    Adapted from https://stackoverflow.com/a/44960748/8706250
    This converts a given wavelength of light to an
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 760 nm
    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    Additionally alpha value set to 0.5 outside range
    """

    wavelength = float(wavelength)
    if 380 <= wavelength <= 760:
        A = 1.
    else:
        A = 0.5
    if wavelength < 380:
        wavelength = 380.
    if wavelength > 760:
        wavelength = 760.
    if 380 <= wavelength <= 450:  # purple
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (450 - 380)
        R = ((-(wavelength - 450) / (450 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif 450 <= wavelength <= 500:  # blue
        R = 0.0
        G = ((wavelength - 450) / (500 - 450)) ** gamma
        B = 1.0
    elif 500 <= wavelength <= 570:  # green
        R = 0.0
        G = 1.0
        B = (-(wavelength - 500) / (570 - 500)) ** gamma
    elif 570 <= wavelength <= 591:  # yellow
        R = ((wavelength - 570) / (570 - 591)) ** gamma
        G = 1.0
        B = 0.0
    elif 591 <= wavelength <= 610:  # orange
        R = 1.0
        G = (-(wavelength - 610) / (610 - 591)) ** gamma
        B = 0.0
    elif 610 <= wavelength <= 760:  # red
        attenuation = 0.3 + 0.7 * (760 - wavelength) / (760 - 610)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    return (R, G, B, A)


clim = (380, 760)
norm = plt.Normalize(*clim)
wl = np.arange(clim[0], clim[1] + 1, 2)
colorlist = list(zip(norm(wl), [wavelength_to_rgb(w) for w in wl]))
spectralmap = matplotlib.colors.LinearSegmentedColormap.from_list("spectrum", colorlist)
