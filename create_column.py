import pandas as pd
from openpyxl.workbook import workbook

def description():
    program_description = """
    How to create a column which storage as a result of a calculation
    """
# df[new_column] = df[column].apply(lambda x: math expression)

def add_hdr():
    column_names = ['First','Last', 'Address','City','State','Area Code','Income']
    df_csv = pd.read_csv('Exercise_Files/Names.csv', header=None)
    df_csv.columns = column_names

    return df_csv

def new_column():
    new_column = input('Type the name of the new column: ')
    return new_column


def run():
    print(new_column())


if __name__ == "__main__":
    run()