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

# Import dataframe df
df = add_hdr()

# Run first condition. List columns
def col_list():
    column_list = list(df.columns)
    return column_list

def choose_column01():
    col_01 = 'City'
    return col_01

def choose_column02():
    col_01 = 'First'
    return col_01

# Filter
def filter_data():
    col_01 = choose_column01()
    col_02 = choose_column02()
    data = df.loc[(df[col_01] == 'Riverside') & (df[col_02] == 'John')]
    return data 

def run():
    print(description())
    print(col_list())
    print(filter_data())

if __name__ == "__main__":
    run()