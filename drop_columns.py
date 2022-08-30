import pandas as pd
from openpyxl.workbook import workbook
from add_header import add_hdr

def description():
    program_description ="""
    This program shows How to drop columns creating a list
    and create a new dataset.
    df.drop(columns=, inplace=True)
    """
    return program_description

# global variables
df = add_hdr()

# Create a list of columns. This list will be dropped from df
col_list = list(df.columns)

# Create a list from a selection
def drop_list():
    to_drop = ['Area Code','First']
    return to_drop

def new_df():
    to_drop = drop_list()
    new_df = df.drop(columns=to_drop,inplace=True)
    return new_df

def run():
    print(description())
    print(col_list)
    print(drop_list())
    print(new_df())


if __name__ == "__main__":
    run()