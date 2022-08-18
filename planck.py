import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k, pi

import warnings

plt_params = {
    'font.size': 14.0,
    'lines.linewidth': 3.0,
    'axes.labelsize': 'large',
    'axes.titlesize': 'x-large',
    'axes.facecolor': 'white',
    'figure.facecolor': 'white',
    'figure.autolayout': True,
    'figure.titlesize': 'xx-large',
    'figure.figsize': (12, 8),
    'legend.fancybox': True,
    'legend.shadow': False,
    'legend.fontsize': 'small',
    'axes.grid': True,
    'axes.axisbelow':True,
    'grid.alpha': 0.3,
    'grid.linestyle': ':',
    'grid.linewidth': 1.5,
}

plt.rcParams.update(plt_params)


class Planck:
    """
    Planck's law
    """

    def __init__(self, wavelengths, temperatures):
        """
        Parameters
        ----------
        wavelengths : array-like
            wavelength array in meters
        temperatures : array-like
            temperature in Kelvin. If only one, pass as a list with the value,
            e.g. [5000]. Or as a tuple with the value, e.g. (5000, ).
        """
        self.wavelengths = wavelengths
        self.temperatures = temperatures

    @staticmethod
    def energy_density(wavelength, temperature):
        """Spectral energy density according to Planck's law.
        Uses the SI unit system, so the wavelength must be in meters (m) and the
        temperature must be in Kelvin (K). Returns the spectral energy density form
        of the Planck's law in Joule per cubic meter per spectral unit.

        Parameters
        ----------
        wavelength : float or np.array
            The wavelength(s) in meter. Accepts vectors or floats
        temperature : float
            Temperature in Kelvin.

        Returns
        -------
        array or float
            Spectral energy density vector or float (depends on wavelength)
        """
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', RuntimeWarning)  # suppress exp overflow
            rho = (8 * pi * h * c) / (wavelength**5 * (np.exp((h * c) /
                                                              (wavelength * k *
                                                               temperature)) - 1))
        return rho

    @staticmethod
    def plot_visible(lines=200, transparency=0.3, unit_exponent=1e9):
        """Plots a visible spectrum in the current axis. Must be called before the
        desired plot.

        Parameters
        ----------
        lines : int, optional
            The number of lines. Increase if blank spaces are noted, by default 200
        transparency : float, optional
            The transparency of the lines, by default 0.3
        unit_exponent : float, optional
            Usually the plots are in nanometers so by default 1e9.
        """
        ax = plt.gca()
        steps = lines
        visible = np.linspace(380e-9, 760e-9, steps)
        colormap = plt.cm.gist_rainbow
        colors = [colormap(i) for i in np.linspace(0.0, 1.0, steps)]
        j = 0
        for val in visible:
            ax.axvline(val * unit_exponent,
                       color=colors[-j], alpha=transparency, zorder=-1)
            j += 1

    def _plot_one_temperature(self, wavelengths, temperature):

        result = self.__class__.energy_density(wavelengths, temperature)

        ax = plt.gca()  # gets the current axes
        ax.plot(wavelengths * 1e9, result, label='{} K'.format(temperature))

        return ax

    def plot(self, colors=plt.cm.coolwarm, ax=None, **visible_kwargs):
        """Plots the Planck's law. The plot is in SI units (wavelength will appear
        in nanometer).

        Parameters
        ----------
        colors : matplotlib colormap, optional
            Desired colormap, by default plt.cm.coolwarm
        ax : matplotlib axis
            If None, it will be created. Default: None
        **visible_kwargs
            Additional keyword arguments passed to `plot_visible` method. See it for
            details.
        """
        if ax is None:
            fig, ax = plt.subplots()

        self.__class__.plot_visible(**visible_kwargs)

        colormap = colors
        ax.set_prop_cycle(plt.cycler('color', colormap(
            np.linspace(0, 1, len(self.temperatures)))))

        for temperature in self.temperatures:
            self._plot_one_temperature(self.wavelengths, temperature)
            ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

        # setting the y-axis to scientific notation and
        # getting the order of magnitude
        ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        ax.yaxis.major.formatter._useMathText = True
        ax.figure.canvas.draw()  # Updates the text
        order_magnitude = ax.yaxis.get_offset_text().get_text().replace('\\times',
                                                                        '')
        ax.yaxis.offsetText.set_visible(False)

        ax.set_xlabel('Wavelength / nm')
        ax.set_ylabel('Energy density / (' + order_magnitude +
                      ' $J/m^3$)')
        ax.set_title('Planck\'s law - black body radiation')

    @classmethod
    def plot_interactive(cls, wavelengths, temperature=0, **visible_kwargs):
        """Method created to be used in interactive plots (like ipywidgets)

        Parameters
        ----------
        wavelengths : array-like
            wavelength array in meters
        temperature : int, optional
            Initial temperature in the plot, by default 0
        **visible_kwargs
            Additional keyword arguments passed to `plot_visible` method. See it for
            details.
        """
        cls(wavelengths, (temperature,)).plot(**visible_kwargs)

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    wavelengths = np.linspace(1.0e-9, 2.0e-6, 1000)
    temperatures = np.arange(1000, 7001, 500)
    example = Planck(wavelengths, temperatures)
    fig1 = plt.figure(figsize=(10, 6))
    ax = fig1.add_subplot(111)
    example.plot(ax=ax)
    plt.show()

