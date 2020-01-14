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
                colors=plt.cm.coolwarm,
                tick_fontsize=14,
                axes_fontsize=14,
                title_fontsize=16):

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
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=14)

    # setting the y-axis to scientific notation and
    # getting the order of magnitude
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax.yaxis.major.formatter._useMathText = True
    ax.figure.canvas.draw()  # Update the text
    order_magnitude = ax.yaxis.get_offset_text().get_text().replace('\\times',
                                                                    '')
    ax.yaxis.offsetText.set_visible(False)

    # labels and title
    ax.set_xlabel('Wavelength / nm', fontsize=axes_fontsize)
    ax.set_ylabel('Energy density / (' + order_magnitude +
                  ' $J/m^3$)', fontsize=axes_fontsize)
    ax.tick_params(labelsize=tick_fontsize)
    ax.set_title('Planck\'s law - black body radiation',
                 fontsize=title_fontsize)

    plt.tight_layout()
    plt.show()


def plot_planck_interactive(wavelength_array,
                            temperature=0):

    plt.figure(figsize=(10, 6))
    plot_visible()
    results = planck_energy_density(wavelength_array, temperature)

    # gets the current axes and set a colormap
    ax = plt.gca()

    # grid lines
    ax.axhline(color="gray", zorder=-1)
    ax.axvline(color="gray", zorder=-1)
    ax.grid(linestyle=':', linewidth=1.5)

    # the plots and legend
    ax.plot(wavelength_array * 1e9, results,
            label='{} K'.format(temperature), linewidth=3)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=14)

    # setting the y-axis to scientific notation and
    # getting the order of magnitude
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax.yaxis.major.formatter._useMathText = True
    ax.figure.canvas.draw()  # Update the text
    order_magnitude = ax.yaxis.get_offset_text().get_text().replace('\\times',
                                                                    '')
    ax.yaxis.offsetText.set_visible(False)

    # labels and title
    ax.set_xlabel('Wavelength / nm', fontsize=14)
    ax.set_ylabel('Energy density / (' + order_magnitude +
                  ' $J/m^3$)', fontsize=14)
    ax.tick_params(labelsize=14)
    ax.set_title('Planck\'s law - black body radiation',
                 fontsize=16)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    lambda_array = np.linspace(1.0e-9, 2.0e-6, 1000)
    temperature_array = np.arange(1000, 7001, 500)
    fig1 = plt.figure(figsize=(10, 6))
    ax = fig1.add_subplot(111)
    plot_visible()
    plot_planck(lambda_array, temperature_array)
