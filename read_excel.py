import pandas as pd
from openpyxl.workbook import workbook

def read_excel():
    df_excel = pd.read_excel('Exercise_Files/regions.xlsx')

    return df_excel

def run():
    print(read_excel())

if __name__ == '__main__':
    run()