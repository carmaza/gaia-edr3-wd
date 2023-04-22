# Distributed under the MIT License.
# See LICENSE for details.
"""
Defines the function :func:`.extract_high_confidence_candidates`.

"""

def extract_high_confidence_candidates(table, pwd=0.75, sdss_spec=True,
                                       sdss_clean=True):
    """
    Select and extract high-confidence WD candidates from catalogue, by giving
    cuts in value to the following quality parameters:

    ``pwd``
        Minimum probability of being a WD (GF+21, Sec. 2).

    ``sdss_spec``
        whether to limit extraction to sources with SDSS spectroscopy only.

    ``sdss_clean``
        whether to limit extraction to clean SDSS photometry only.

    Parameters
    ----------

    table : astropy.table.table.Table
        The raw table extracted from the catalogue (e.g. using the function
        :func:`.table_from_fits`.

    pwd : float
        (Optional) The minimum probability of being a WD. Default: 0.75.

    sdss_spec : bool
        (Optional) Whether to limit extraction to sources with known SDSS
        spectroscopy only. Default: True.

    sdss_clean : bool
        (Optional) Whether to limit extraction to sources with clean SDSS
        photometry only. Default: True.

    Returns
    -------

    out : astropy.table.table.Table
        A new table containing only high-confidence white dwarfs candidates.

    Notes
    -----

    - Input raw table (1,280,266 rows) is NOT mutated by this function.

    - As a guideline, the value of 0.75 gives 359,074 candidates, of which
      25,632 have SDSS spectroscopy available. (Catalog retrieved on 04/20/23.)
      Higher values of ``pwd`` may produce cleaner but less complete sets.

    """

    table = table[table["Pwd"] >= pwd]

    # Number of SDSS spectra available for each source (GF+21 Table 2, row 160).
    if sdss_spec:
        table = table[table["SDSS_spec"] >= 1]

    # Value of 1 is a convention in the catalog (GF+21, Table 2, row 148).
    if sdss_clean:
        table = table[table["sdss_clean"] == 1]

    return table
