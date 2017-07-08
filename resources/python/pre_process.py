#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pandas as pd


def main():
    """Returns a new csv file
    containing the processed data
    """

    # Get annual production
    directory = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
    p_file_loc = os.path.join(directory, "data", "production-yearly-by-field.csv")
    df_prod = pd.read_csv(p_file_loc)

    # Get total reserves
    res_file_loc = os.path.join(directory, "data", "reserves.csv")

    df_reserv = pd.read_csv(res_file_loc)

    print("Finished")

if __name__ == '__main__':
    main()
