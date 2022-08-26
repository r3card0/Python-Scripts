import pandas as pd
from openpyxl.workbook import workbook

def read_csv():
    df_csv = pd.read_csv('Exercise_Files/Names.csv')

    return df_csv

def run():
    print(read_csv())

if __name__ == '__main__':
    run()