import warnings

from astropy.io import fits
from astropy.table import Table


def read(path="GaiaEDR3_WD_main.fits"):
    """
    Read catalogue of white dwarfs in Gaia EDR3.
    N. P. Gentille Fusillo et al. 2021

    MNRAS 508, 3877–3896 (2021)
    https://doi.org/10.1093/mnras/stab2672

    """

    # 'astropy.io.fits.hdu.hdulist.HDUList' object.
    hdul = fits.open(path)

    # 'astropy.io.fits.hdu.table.BinTableHDU' object.
    bintable = hdul[1]

    # 'astropy.table.table.Table' object.
    table = Table.read(bintable)

    for colname in table.colnames:
        if "mass" in colname:
            print(colname)


read()
