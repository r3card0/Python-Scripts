# This program returns values by selecting
# a property taken from a column

import pandas as pd
from openpyxl.workbook import workbook

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
    column_selected = input("Select a column: ")
    return column_selected

def column_values():
    df = add_hdr()
    column = select_column()
    values = df[column].unique()
    message = f'The values of {column} are: {values}'
    return message

def select_value():   
    value_selected = input("Select a value: ")
    return value_selected

def print_data():
    # df.loc[df['column_name'] == 'property value']
    df = add_hdr()
    print(menu())
    column = select_column() 
    
    values = df[column].unique()
    message = f'The values of {column} are: {values}'
    print(message)

    value = select_value()
    data = df.loc[df[column] == value]

    return data

def run():
    print(print_data())

if __name__ == "__main__":
    run()