import pandas as pd
from openpyxl.workbook import workbook
from add_header import add_hdr

# How to view values from a single row

def row_value():
    df_csv = add_hdr()
    row_cnt = len(df_csv.index)-1
    print(f'Data frame has {row_cnt} rows')
    try:
       # def select_show():
        row_index = int(input('Select an index-row: '))
        show_row = df_csv.iloc[[row_index]]

        return show_row

    except ValueError:
        print('ValueError:invalid literal for int()')

    return f'run again' 

    # return show_row


def run():
    print(row_value())


if __name__ == '__main__':
    run()