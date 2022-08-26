import pandas as pd
from openpyxl.workbook import workbook

# indicates first line is not a header

def none_hdr():
    df_csv = pd.read_csv('Exercise_Files/Names.csv', header=None)

    return df_csv

def run():
    print(none_hdr())

if __name__ == '__main__':
    run()