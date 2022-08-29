# enlistar df
# elegir columna
# elegir property
# print all values with property in column


import pandas as pd
from openpyxl.workbook import workbook

# df.loc[df['column_name'] == 'property value']

def add_hdr():
    column_names = ['First','Last', 'Address','City','State','Area Code','Income']
    df_csv = pd.read_csv('Exercise_Files/Names.csv', header=None)
    df_csv.columns = column_names

    return df_csv

def columns():
    df_csv = add_hdr()
    columns_list = list(df_csv.columns)

    return columns_list

def menu():
    columns_list = columns()
    message = f"""
    Columns list: {columns_list}
    """

    return message

def select_column():
    print(menu())
    column_selected = input("Select a column: ")

    return column_selected

def column_values():
    df = add_hdr()
    column = select_column()
    values = df[column].unique()
    message = f'The values of {column} are: {values}'

    return message
# lista las propiedades de la columna elegida

def select_value():
    column = select_column()    
    value_selected = input(f"Select a {column}: ")

    return value_selected

def print_data():
    # df.loc[df['column_name'] == 'property value']
    df =add_hdr()
    column = select_column()
    value = select_value()
    data = df.loc[df[column] == value]

    return data

def run():
    print(column_values())

if __name__ == "__main__":
    run()