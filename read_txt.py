# This program reads a txt file

import pandas as pd
from openpyxl.workbook import workbook

def read_txtf():
    df_txt = pd.read_csv('Exercise_Files/data.txt')

    return df_txt

def run():
    print(read_txtf())


if __name__ == '__main__':
    run()