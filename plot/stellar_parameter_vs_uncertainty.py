# Distributed under the MIT License.
# See LICENSE for details.
"""
Defines function :func:`.stellar_parameter_vs_uncertainty`.

"""

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Latin Modern Roman"
plt.rcParams["mathtext.fontset"] = "cm"


def stellar_parameter_vs_uncertainty(table, parameter, composition):
    """
    Plot a stellar parameter vs its uncertainty.

    Parameters
    ----------

    table : astropy.table.table.Table
        The table containing the data.

    parameter : str
        The stellar parameter to plot. Must be one of 'mass' (stellar
        mass in solar units), 'teff' (effective temperature in kelvins),
        or 'logg' (log of surface gravity, in cm/s^2).

    composition : str
        The atmospheric composition used to calculate the stellar parameter
        (GF+21, Sec 4). Must be one of 'H' (pure H), 'He' (pure He), or
        'mixed' (mixed H and He).

    """
    print(f"Plotting {parameter} vs uncertainty...")

    available_parameters = ["mass", "teff", "logg"]
    if not parameter in available_parameters:
        msg = f"""
        Parameter '{parameter}' not available in catalog.
        Available parameters: {available_parameters}.
        """
        raise ValueError(msg)

    available_compositions = ["H", "He", "mixed"]
    if not composition in available_compositions:
        msg = f"""
        Parameter '{composition}' not available in catalog.
        Available parameter types: {available_compositions}.
        """
        raise ValueError(msg)

    parameter_tag = f"{parameter}_{composition}"
    parameter_sigma_tag = f"e{parameter}_{composition}"

    columns_kept = [parameter_tag, parameter_sigma_tag, "Pwd"]

    table.keep_columns(columns_kept)

    param = table[parameter_tag]
    sigma = table[parameter_sigma_tag]

    fig, ax = plt.subplots(1, 1, figsize=(5, 3))

    colormap = ax.scatter(param,
                          sigma,
                          s=0.1,
                          marker=',',
                          c=table["Pwd"],
                          cmap="inferno_r")

    cbar = fig.colorbar(colormap, ax=ax)
    cbar.ax.set_title(r"$P_{WD}$")

    labels = {}
    labels["mass"] = {
        "x": r"mass [$M_\odot$]",
        "y": r"uncertainty [$M_\odot$]"
    }
    labels["teff"] = {"x": r"$T_\mathrm{eff}$ [K]", "y": r"uncertainty [K]"}
    labels["logg"] = {
        "x": r"log(surface gravity / [cm s$^{-2}$])",
        "y": r"log(uncertainty / [cm s$^{-2}$])"
    }

    ax.set_xlabel(labels[parameter]["x"])
    ax.set_ylabel(labels[parameter]["y"])

    ax.set_yscale("log")

    filename = f"{parameter.capitalize()}VsSigma{composition.capitalize()}.pdf"
    plt.savefig(filename, bbox_inches="tight", dpi=60)

    print(f"Plot file {filename} saved.")
    plt.close(fig)
