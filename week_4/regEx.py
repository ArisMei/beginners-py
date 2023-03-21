# import os
# new_directory = "C:\\Users\\User\\OneDrive - Universidad Politécnica de Madrid\\Aalto\\beginners-Py\\week_4"
# os.chdir(new_directory)
# os.getcwdb()

# Template code for Exercise "regEx"

import pandas as pd

# df = pd.read_csv("small_dataset.csv")

"""
Complete the missing regular expression (regex = ) arguments between the quotation marks "",
so as to filter the dataset to provide the described subset. You may edit the main program to
create your own tests. Do not modify the test functions beyond the regex variable definition.
"""

"""
In task1, the program needs to print all the usernames starting with uppercase or lowercase vowels
"""
def test1(df):
    # fill in here for usernames starting with vowels

    regex = r"\b[aeiouAEIOU]\w*\b"

    filtered = str(df[df["Username"].str.match(regex)])
    return filtered

"""
In task2, the program needs to print all the usernames that contain 2 consecutive vowels.
"""
def test2(df):
    # fill in here for usernames having 2 consecutive vowels

    regex = r"\b\w*[aeiouAEIOU]{2}\w*\b"

    filtered = str(df[df["Username"].str.match(regex)])
    return filtered

"""
In task3, the program needs to print all the usernames that do not contain any special characters (i.e. anything except alphabetic or numeric characters)."""


def test3(df):
    # fill in here for usernames not containing any special characters

    regex = r"^[a-zA-Z0-9]+$"

    filtered = str(df[df["Username"].str.match(regex)])
    return filtered

"""
In task4, the program needs to print all the usernames that end with a numeric digit
"""
def test4(df):
    # fill in here for usernames ending with a number

    regex = r"\b\w*[0-9]+\b"

    filtered = df[df["Username"].str.contains(regex)]
    return filtered.to_string(index=True)

"""
In task5, the program needs to print all the usernames, such that they start with "AG", followed by an underscore (_), followed by an uppercase alphabetic character, and eventually ending with two numerical values. For example, "AG_Kfhab70" would be a valid username whereas "AG_fazebanks9" would not.
"""
def test5(df):
    # Filter the dataset to match the following pattern:
    # AG_Tambo19
    # AG_Rex17
    # AG_Peeta13
    # AG_Orneal22
    # AG_Karl05

    # Example invalid entries such as:
    # AH_Tambo19
    # AG-Rex17
    # AG_peeta13
    # AG_Orneal2
    # AG_Karl5
   

    regex = r"\bAG_[A-Z]\w*\d{2}\b"

    filtered = str(df[df["Username"].str.match(regex)])
    return filtered


def main():
    filename = input("Enter the name of the file to be read:\n")

    try:
        df = pd.read_csv(filename)
        print("\nOutput from function 1: \n" + test1(df))
        print("\nOutput from function 2: \n" + test2(df))
        print("\nOutput from function 3: \n" + test3(df))
        print("\nOutput from function 4: \n" + test4(df))
        print("\nOutput from function 5: \n" + test5(df))

    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))

if __name__ == "__main__":
    main()


