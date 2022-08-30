import pandas as pd
from openpyxl.workbook import workbook
from add_header import add_hdr

def description():
    program_description = """
    This program  filter a dataframe taken two properties 
    as conditions
    df.loc[(df[column01] == 'cond1) & (df[column02] == cond2)]
    """
    return program_description

df = add_hdr()

def run():
    print(description())

if __name__ == "__main__":
    run()