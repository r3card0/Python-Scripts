import pandas as pd
from openpyxl.workbook import workbook
from read_txt import read_txt

def tab_delimiter():
    text_file = read_txt()
    df_txt = pd.read_csv('Exercise_Files/data.txt', delimiter='\t')

    return df_txt

def run():
    print(tab_delimiter())

if __name__ == '__main__':
    run()
