import pandas as pd
from openpyxl.workbook import workbook
from add_header import add_hdr
# how to view the values of a column

def col_value():
    df_csv = add_hdr()
    print(df_csv.columns)
    choose_col = input('Choose a column: ')
    choosed_col = df_csv[[choose_col]]
    
    return choosed_col #watch_columns #df_csv

def run():
    print(col_value())


if __name__ == '__main__':
    run()