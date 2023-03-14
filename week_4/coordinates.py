# Path: week_4\coordinates.py
# import os
# new_directory = "C:\\Users\\User\\OneDrive - Universidad Politécnica de Madrid\\Aalto\\beginners-Py\\week_4"
# os.chdir(new_directory)
# os.getcwdb()

import pandas as pd
import numpy as np

def is_file_exists(filename):
    try:
        with open(filename) as file:
            return True
    except FileNotFoundError:
        return False


def decimal_to_dms_latitude(decimal_degrees):
    degrees = int(decimal_degrees)
    minutes = int((decimal_degrees - degrees) * 60)
    seconds = (decimal_degrees - degrees - minutes / 60) * 3600
    cardinal = "N" if degrees >= 0 else "S"  # North for positive degrees, South for negative degrees
    dms = '''{}° {}' {:.2f}" {}'''.format(abs(degrees), abs(minutes), abs(seconds), cardinal)
    return dms

def decimal_to_dms_longitude(decimal_degrees):
    degrees = int(decimal_degrees)
    minutes = int((decimal_degrees - degrees) * 60)
    seconds = (decimal_degrees - degrees - minutes / 60) * 3600
    cardinal = "E" if degrees >= 0 else "W"  # North for positive degrees, South for negative degrees
    dms = '''{}° {}' {:.2f}" {}'''.format(abs(degrees), abs(minutes), abs(seconds), cardinal)
    return dms
    


# In the given files, the coordinates are provided in simple
# decimal degrees. We would like to convert these decimal 
# degrees into degrees, minutes, and seconds, and to present
# the result as a string

def main():
    while True:
        filename = input("Enter the name of the file to be read:\n")
        if (is_file_exists(filename)):
            print("File read successfully.")
            print("Conversions are as follows:")
            df = pd.read_csv(filename)
            #print(df)
            latitudes = list(map(decimal_to_dms_latitude, df['Latitude']))
            longitudes = list(map(decimal_to_dms_longitude, df['Longitude']))
            values = list(zip(latitudes,longitudes))
            #print(values)
            for i in range(len(df['City'])):
                print("{:s}: {:s},{:s}".format(df['City'][i],latitudes[i],longitudes[i]))
            break
        else:
            print("Error in readinf the file {:s}. Pleas try again".format(filename))


main()


