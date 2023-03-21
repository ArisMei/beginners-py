import os
new_directory = "C:\\Users\\User\\OneDrive - Universidad Politécnica de Madrid\\Aalto\\beginners-Py\\week_4"
os.chdir(new_directory)
os.getcwdb()

import pandas as pd

"""
Complete the missing regular expression (regex = ) arguments between the quotation marks ""
so as to filter the dataset to provide the described subset. Do not modify the test 
functions beyond the regex variable definition.

TASK:

- Imagine that you are restricted to an alphabet made up of the following: "W" "A" "P" "U" 

- Any combination of these letters is acceptable as long 
  as "U" is never followed by a "W" or "U", nor "A" followed by an "P" or "A".
"""

def challenge(dataset):


    regex = r"^[WAP]*((?!U[WU]|A[P|A])[WAP])*U?"


    return str(dataset[dataset["Words"].str.match(regex)])

print("Output: " + challenge(pd.read_csv("challengeSetA.csv")))
