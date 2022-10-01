import pandas as pd


def description():
    program_description = """
    This program returns a dataframe with openpyxl commands and their explanations and use
    """
    return program_description

commands = ["Workbook()","create_sheet","active", "load_workbook","active_sheet", "values"]
use = ["Creates a new workbook","creates a sheet into a workbook","turn on workbook","loads and existin workbook","method to acces to a worksheet?","returns a value"]

def commands():
    commands_dict= {
        "commands":  ["Workbook()","create_sheet","active", "load_workbook","active_sheet", "values"],
        "use" : use,
    }

    return commands_dict


def dataframe():
    df = pd.DataFrame(commands())
    return df

def run():
    print(dataframe())


if __name__ == "__main__":
    run()