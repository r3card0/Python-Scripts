import pandas as pd
from openpyxl.workbook import workbook

def description():
    program_description = """
    This program creates a new column by applying a function to an existing column
    Function -> lambda x: 0.15 if 10000 < x < 40000 else 0.2 if 40000 < x < 80000 else 0.25
    """
    return program_description

# df[new_column] = df[column].apply(lambda x: math expression)

def add_hdr():
    column_names = ['First','Last', 'Address','City','State','Area Code','Income']
    df_csv = pd.read_csv('Exercise_Files/Names.csv', header=None)
    df_csv.columns = column_names

    return df_csv

def column_name():
    column_name = input('Type the name of the new column: ')
    return column_name

def expression():
    new_expression = input('Type the expression to calculate result: ')
    return new_expression

def select_column():
    column_selected = input("Select a column: ")
    return column_selected

def columns():
    df_csv = add_hdr()
    columns_list = list(df_csv.columns)
    return columns_list

# df[new_column] = df[column].apply(lambda x: math expression)
def new_column():
    print(description())
    df = add_hdr()
    col_name = column_name()
    print(columns())
    col_selected = select_column()
    #new_expression = expression()
    df[col_name] = df[col_selected].apply(lambda x: 0.15 if 10000 < x < 40000 else 0.2 if 40000 < x < 80000 else 0.25)

    return df

def run():
    print(new_column())


if __name__ == "__main__":
    run()