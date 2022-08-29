# enlistar df
# elegir columna
# elegir property
# print all values with property in column


import pandas as pd
from openpyxl.workbook import workbook

def add_hdr():
    column_names = ['First','Last', 'Address','City','State','Area Code','Income']
    df_csv = pd.read_csv('Exercise_Files/Names.csv', header=None)
    df_csv.columns = column_names

    return df_csv

def select_column():
    df_csv = add_hdr()
    columns_list = list(df_csv.columns)

    return columns_list


def run():
    print(select_column())

if __name__ == "__main__":
    run()