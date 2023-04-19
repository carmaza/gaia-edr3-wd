# Distributed under the MIT License.
# See LICENSE for details.
"""
Defines function :func:`.table_from_fits`.

"""

import warnings

from astropy.io import fits
from astropy.table import Table


def table_from_fits(path="GaiaEDR3_WD_main.fits"):
    """
    Read catalogue of white dwarfs in Gaia EDR3 and return table.

    N. P. Gentille Fusillo et al. 2021 (GF+21)
    MNRAS 508, 3877–3896 (2021)
    https://doi.org/10.1093/mnras/stab2672

    Parameters
    ----------

    path : str
        The path to the catalogue, including filename and FITS extension.

    Returns
    -------

    out : astropy.table.table.Table
        The catalogue as a table.

    """

    # 'astropy.io.fits.hdu.hdulist.HDUList' object.
    hdul = fits.open(path)

    # 'astropy.io.fits.hdu.table.BinTableHDU' object.
    bintable = hdul[1]

    print(f"Opened file {path}.")

    # Creating a new table from the catalogue provided by GF+21 throws some
    # `UnitsWarning`s associated to units impossible to parse as fits units.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        print("Creating table from catalogue...")

        # 'astropy.table.table.Table' object.
        table = Table.read(bintable)

    print("Table created.")
    return table
