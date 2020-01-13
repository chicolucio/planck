import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k, pi


def planck_energy_density(wavelength, temperature):
    rho = (8 * pi * h * c) / (wavelength**5 * (np.exp((h * c) /
                                                      (wavelength * k *
                                                       temperature)) - 1))
    return rho


def plot_visible(lines=100, transparency=0.3, linewidth=3, unit_exponent=1e9):
    ax = plt.gca()
    steps = lines
    visible = np.linspace(380e-9, 760e-9, steps)
    colormap = plt.cm.gist_rainbow
    colors = [colormap(i) for i in np.linspace(0.0, 1.0, steps)]
    j = 0
    for val in visible:
        ax.axvline(val * unit_exponent, lw=linewidth,
                   color=colors[-j], alpha=transparency, zorder=-1)
        j += 1


def plot_planck(wavelength_array,
                temperature_array,
                colors=plt.cm.coolwarm):

    results = []
    for temperature in temperature_array:
        results.append(planck_energy_density(wavelength_array, temperature))

    # gets the current axes and set a colormap
    ax = plt.gca()
    colormap = colors
    ax.set_prop_cycle(plt.cycler('color', colormap(
        np.linspace(0, 1, len(temperature_array)))))

    # grid lines
    ax.axhline(color="gray", zorder=-1)
    ax.axvline(color="gray", zorder=-1)
    ax.grid(linestyle=':', linewidth=1.5)

    # the plots and legend
    for result, temperature in zip(results, temperature_array):
        ax.plot(wavelength_array * 1e9, result,
                label='{} K'.format(temperature), linewidth=3)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

    # setting the y-axis to scientific notation and
    # getting the order of magnitude
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax.yaxis.major.formatter._useMathText = True
    ax.yaxis.offsetText.set_visible(False)

    plt.draw()  # Update the text
    order_magnitude = ax.yaxis.get_offset_text().get_text().replace('\\times',
                                                                    '')

    # labels and title
    ax.set_xlabel('Wavelength / nm')
    ax.set_ylabel('Energy density / (' + order_magnitude + ' $J/m^3$)')
    ax.set_title('Planck\'s law - black body radiation')

    # relative font sizes
    plt.rcParams.update({'axes.titlesize': 'xx-large',
                         'axes.labelsize': 'xx-large',
                         'xtick.labelsize': 'x-large',
                         'ytick.labelsize': 'x-large',
                         'legend.fontsize': 'large'})
    plt.draw()
    plt.tight_layout()
    plt.show()
