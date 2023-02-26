# -*- coding: utf-8 -*-
"""
Author: Benedikt Goodman
Email: bgo@ssb.no
Created: 24.02.2023

"""


def test_associate_codes(df, ind_code_col, nr_code_col):
    """
    Test whether the one-to-many mapping was successful.

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe containing source data and new column w/ new codes.
    ind_code_col : str
        Dataframe column containing codes that were mapped to new column.
    nr_code_col : str
        Dataframe column containing new codes.

    Returns
    -------
    bool
        True if one-to-many mapping was successful, False otherwise.
    """

    # Group by the original codes and check if there are any duplicates in the new codes
    group = df.groupby(ind_code_col)[nr_code_col].nunique()
    duplicates = group[group > 1]

    # If there are any duplicates, the one-to-many mapping was not successful
    if not duplicates.empty:
        print(f"Error: The following {ind_code_col} codes were mapped to multiple {nr_code_col} codes:")
        print(duplicates)
        return False

    # Otherwise, the one-to-many mapping was successful
    return True


def missing_nrnaaring_tester(df):
    """
    Check for missing values in the 'nr_naaring' column of a Pandas DataFrame where 'est_avgift_kroner' is not 0.

    Parameters
    ----------
    df_in : pandas.DataFrame
        Input DataFrame to check for missing values.

    Returns
    -------
    pandas.DataFrame or pandas.Series
        If any missing values are found, a warning message is printed and the dataframe is returned.
        Otherwise, the original input DataFrame is returned.

    Notes
    -----
    This function checks for missing values in the 'nr_naaring' column of a Pandas DataFrame, but only for cases where
    the 'est_avgift_kroner' column is not equal to 0. The function returns a copy of the input DataFrame and creates boolean 
    masks to select rows that meet these conditions. It then uses the .loc[] method to count the number of missing rows 
    that meet both conditions. If any rows are found, a warning message is printed and the missing rows are returned. 
    Otherwise, the original input DataFrame is returned.
    """

    mask_1 = df['est_avgift_kroner']  != 0
    mask_2 = df['nr_naaring'].isna()

    missing = len(
        df.loc[(mask_1) & (mask_2)]
    )

    if missing > 0:
        print('Warning! The following nr_naaring codes have not beeen successfully mapped to a NACE code')
        print(df.loc[(mask_0) & (mask_2)])
        return df

    else:
        return df