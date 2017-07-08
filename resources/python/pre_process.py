#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pandas as pd


def main():
    """Returns a new csv file
    containing the processed data

    Function will take seperate
    csv files and combine these into a
    new table.

    This is designed specifically for
    producing a dataset for visualisation.
    """

    directory = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
    
    # Get annual production
    p_file_loc = os.path.join(directory, "data", "production-yearly-by-field.csv")
    df_prod = pd.read_csv(p_file_loc, sep=';')

    # Get monthly production
    pm_file_loc = os.path.join(directory, "data", "production-monthly-by-field.csv")
    dfm_prod = pd.read_csv(pm_file_loc, sep=';')

    # Get total reserves
    res_file_loc = os.path.join(directory, "data", "reserves.csv")
    df_reserv = pd.read_csv(res_file_loc, sep=';')

    # Get field status, including year approved for production
    stat_file_loc = os.path.join(directory, "data", "status.csv")
    df_status = pd.read_csv(stat_file_loc, sep=';')

    # Calculate cumlative production for each field(groupby category)
    df_prod["cumalative_prod"] = df_prod.groupby("prfInformationCarrier")["prfPrdOeNetMillSm3"].transform(pd.Series.cumsum)

    def get_reserves(row):
        if row["prfInformationCarrier"] in df_reserv["fldName"].unique():
            return float(df_reserv[df_reserv["fldName"] == row["prfInformationCarrier"]]["fldRecoverableOE"])
        else:
            return "NAN"

    df_prod["reserves"] = df_prod.apply(get_reserves, axis=1)

    print(df_prod.head(100))
    print("Finished")

if __name__ == '__main__':
    main()
