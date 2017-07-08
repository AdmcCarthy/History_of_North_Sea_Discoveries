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


    def cumulative_annual_production():
        """Returns production as
        cumulative, to be used in Pandas
        apply.
        """

        for field in df_prod["prfInformationCarrier"].unique():
            print(field)

        values = 1

        return values

    def reserves_subtraction():
        """To be used in Pandas apply to
        return values based on reserves subtracting
        cumulative production"""

        values = 2

        return values

    cumulative_annual_production()

    print("Finished")

if __name__ == '__main__':
    main()
