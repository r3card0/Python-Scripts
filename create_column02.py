import pandas as pd
from openpyxl.workbook import workbook

def description():
    program_description ="""
    This program creates a new column by multiply two columns from
    dataframe. 

    # df[new_column] = df[column01] * df[column02]   
    """

    return program_description

def add_hdr():
    column_names = ['First','Last', 'Address','City','State','Area Code','Income']
    df_csv = pd.read_csv('Exercise_Files/Names.csv', header=None)
    df_csv.columns = column_names

    return df_csv

def column_name():
    column_name = 'Tax %'
    return column_name

def select_column():
    column_selected = 'Income'
    return column_selected

def new_column():
    print(description())
    df = add_hdr()
    col_name = column_name()
    # print(columns())
    col_selected = select_column()
    #new_expression = expression()
    df[col_name] = df[col_selected].apply(lambda x: 0.15 if 10000 < x < 40000 else 0.2 if 40000 < x < 80000 else 0.25)

    return df

def column_name_2():
    column_name = input('Type the name of the new column: ')
    return column_name

def select_column_1():
    column_selected_1 = input("Select first one column: ")
    return column_selected_1

def select_column_2():
    column_selected_2 = input("Select second one column: ")
    return column_selected_2

# df[new_column] = df[column01] * df[column02]

def column_multiply():
    vis = print(new_column())
    df = new_column()
    col_mul = column_name_2()
    column01 = select_column_1()
    column02 = select_column_2()
    df[col_mul] = df[column01] * df[column02]

    return df


def run():
    #print(description())
    print(column_multiply())

if __name__ == "__main__":
    run()