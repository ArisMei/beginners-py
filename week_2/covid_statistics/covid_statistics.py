# import os.path
# new_directory = "C:\\Users\\User\\OneDrive - Universidad Politécnica de Madrid\\Aalto\\beginners-Py\\week_2\\covid_statistics"
# os.chdir(new_directory)
# os.getcwdb()

import datetime
import pandas as pd
import numpy as np
DATE_FORMATS = ["%Y-%m-%d", "%d.%m.%Y", "%d.%m.%y", "%d-%m-%Y", "%d/%m/%Y", "%m/%d/%Y"]

def get_date_format(dates):
    # Gets a Pandas Series of dates as strings and attempts to convert each string to a DateTime object
    # Conversion is attempted with every format in 'DATE_FORMATS' list
    # Returns a date format that works for all date strings
    for date_format in DATE_FORMATS:
        reject_format = False
        i = 0
        while not reject_format:
            try:
                datetime.datetime.strptime(dates[i], date_format)
                if (i + 1) == len(dates):
                    return date_format
            except ValueError:
                reject_format = True
            i += 1
    raise Exception('An error occurred: no valid date format found.')


def convert_to_int(string_num):
    """Converts a string representation of a number to an integer."""
    try :
        num = string_num.replace(',', '').replace(' ', '').replace('.', '')
        return int(num)
    except ValueError:
        return np.NaN
    
def is_file_exists(filename):
    try:
        with open(filename) as file:
            return True
    except FileNotFoundError:
        return False
    

def main():
    list_dataframes = list()
    list_names = list()
    i = 1
    while i != 4:
        # The program does not ask the user for the file format. Instead, it interprets it from the filename provided (i.e. what file extension does the filename end in – is it .csv, .xls or .json?).
        # The program reads the file and stores the data in a Pandas DataFrame.
        # The program prints out summary statistics using the DataFrame.describe method.
        filename = input("Enter the name of file #{}:\n".format(i))
        if (is_file_exists(filename)):
            if (filename in list_names):
                print("File {:s} is already included in this analysis. Please choose a different file.".format(filename))
            
            else: 
                try:
                    name, extension = map(str, filename.split("."))
                    df = pd.read_csv(filename, sep="\t", dtype=str)
                    df.date = pd.to_datetime(df.date, format = get_date_format(df.date))
                    df.date = df.date.dt.date # Removes time value from DateTime object
                    df.cases = df.cases.apply(convert_to_int)
                    #print(df.cases)
                    df.rename(columns={'cases': 'cases_{:s}'.format(name)}, inplace=True)
                    list_dataframes.append(df)
                    list_names.append(filename)
                    i += 1

                except (ValueError, IndexError):
                    print ("Error in reading the file '{:s}'. Closing program.".format(filename))
                    break
        else:
            print("Error in reading file {:s}. Closing program.".format(filename))
            return
    dfs = [df.set_index('date') for df in list_dataframes]
    dfs = (pd.concat(dfs, axis=1))
    dfs = dfs.reset_index()
    # Printig summary statistics
    print("Printing summary statistics:")
    print(dfs.describe())
    print("\n")
    # Printing the first five rows:
    print("Printing first five rows:")
    print(dfs.head(5))

main()
