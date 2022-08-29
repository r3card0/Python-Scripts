import pandas as pd
from openpyxl.workbook import workbook

# Find all people live on Riverside
# From a selected column, find some property

def add_hdr():
    column_names = ['First','Last', 'Address','City','State','Area Code','Income']
    df_csv = pd.read_csv('Exercise_Files/Names.csv', header=None)
    df_csv.columns = column_names

    return df_csv


def filter_by():
    df = add_hdr() 
    # df.loc[df['column_name'] == 'property value']

    filter_by = df.loc[df['City'] == 'Riverside']

    return filter_by


def run():
    print(filter_by())


if __name__ == "__main__":
    run()
