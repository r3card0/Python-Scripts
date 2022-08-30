import pandas as pd
from openpyxl.workbook import workbook
from add_header import add_hdr
from choose_column import choose_column

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

def column01():
    col_01 = choose_column()
    return col_01

def column02():
    col_01 = choose_column()
    return col_01

def choose_column01():
    col_01 = 'City'
    return col_01

def choose_column02():
    col_01 = 'First'
    return col_01

def column01_values():
    column = column01()
    values = df[column].unique()
    message = f'The values of {column} are: {values}'
    return message

# Filter
def filter_data():
    col_01 = column01()
    #print(column01_values())
    col_02 = column02()
    data = df.loc[(df[col_01] == 'Riverside') & (df[col_02] == 'John')]
    return data 

def run():
    print(description())
    print(col_list())
    print(filter_data())
    #print(column01())

if __name__ == "__main__":
    run()