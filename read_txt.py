import pandas as pd
from openpyxl.workbook import workbook

def read_txt():
    df_txt = pd.read_csv('Exercise_Files/data.txt')

    return df_txt

def run():
    print(read_txt())


if __name__ == '__main__':
    run()