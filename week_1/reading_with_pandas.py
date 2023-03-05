# import os
# import os.path
# import pandas as pd
# new_directory = "C:\\Users\\User\\OneDrive - Universidad Politécnica de Madrid\\Aalto\\beginners-Py\\week_1"
# os.chdir(new_directory)
import pandas as pd

def is_file_exists(filename):
    try:
        with open(filename) as file:
            return True
    except FileNotFoundError:
        return False

def main():
    while True:
        filename = input("Enter the name of the file to be read:\n")
        # The program does not ask the user for the file format. Instead, it interprets it from the filename provided (i.e. what file extension does the filename end in – is it .csv, .xls or .json?).
        # The program reads the file and stores the data in a Pandas DataFrame.
        # The program prints out summary statistics using the DataFrame.describe method.
        try:
            name, extension = map(str, filename.split("."))
            if (extension == "csv" or extension == "xls" or extension == "json"):
                if (extension == "csv" and is_file_exists(filename)):
                    print("File read successfully.\n")
                    print("\n")
                    print("Printing summary statistics:")
                    df = pd.read_csv(filename)
                    print(df.describe())
                    break
                elif (extension == "xls" and is_file_exists(filename)):
                    print("File read successfully.\n")
                    print("\n")
                    print("Printing summary statistics:")
                    df = pd.read_excel(filename)
                    df.describe
                    print(df.describe())
                    break
                elif (extension == "json" and is_file_exists(filename)):
                    print("File read successfully.\n")
                    print("\n")
                    print("Printing summary statistics:")
                    df = pd.read_json(filename)
                    print(df.describe())
                    break
                else :
                    print("Error in reading the file '{:s}'. Please try again.".format(filename))
            else:
                print("File extension '{:s}' is not supported. Please try again".format(extension))

        except (ValueError, IndexError):
            print ("Error in reading the file '{:s}'. Please try again.".format(filename))

main()