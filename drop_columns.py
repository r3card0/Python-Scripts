import pandas as pd
from openpyxl.workbook import workbook
from add_header import add_hdr



def description():
    program_description ="""
    This program shows how to drop a set of columns to create a new 
    dataset.
    df.drop(columns=, inplace=True)
    """
    return program_description

# global variables
df = add_hdr()

# Create a list of columns. This list will be dropped from df
col_list = df.columns

# Create a list from a selection
def drop_list():
    to_drop = ['Area Code','First','Address']
    return to_drop

def run():
    print(description())
    print(drop_list())


if __name__ == "__main__":
    run()