import pandas as pd
from openpyxl.workbook import workbook

def add_hdr():
    column_names = ['First','Last', 'Address','City','State','Area','Code']
    df_csv = pd.read_csv('Exercise_Files/Names.csv', header=None)
    df_csv.columns = column_names

    return df_csv

def run():
    print(add_hdr())

if __name__ == '__main__':
    run()