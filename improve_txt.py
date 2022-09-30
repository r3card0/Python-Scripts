# This program improves the format of a txt file
# Uses flag delimiter=

import pandas as pd
from openpyxl.workbook import workbook
#from read_txt import read_txtf

def tab_delimiter():
    #text_file = read_txtf()
    df_txt = pd.read_csv('Exercise_Files/data.txt', delimiter='\t')

    return df_txt

def run():
    print(tab_delimiter())

if __name__ == '__main__':
    run()
