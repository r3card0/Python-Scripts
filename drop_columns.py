import pandas as pd
from openpyxl.workbook import workbook
from add_header import add_hdr

def description():
    program_description ="""
    This program show how to drop a set of columns to create a new 
    dataset.
    df.drop(columns=, inplace=True)
    """
    return program_description

def run():
    print(description())


if __name__ == "__main__":
    run()