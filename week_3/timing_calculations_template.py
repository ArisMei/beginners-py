import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import time
import math
# import random

## Timing calculations

# The execise is about the following topics:

#   - Using the Time modeule: calculating precessing times for actions
#   - Using the Pandas library: calculating statistics from DataFrames
#   - Using Scikit-learn: calculating simple linear regressions


# Your task is to complete the seven incomplete functions in the given code, namely: 
# 1. measure_time
# 2. calculate_mean_manually
# 3. calculate_sd_manually
# 4. calculate_linreg_manually
# 5. calculate_mean_automatically
# 6. calculate_sd_automatically
# 7. calculate_linreg_automatically.


# The given main function is sufficient – you should not edit it.

# The functions ending in “manually” should only use the built-in functions and mathematical operators of Python 
# (i.e. pandas / NumPy / sklearn should not be used in these functions), while the functions ending in “automatically” 
# should specifically use the libraries’ functions.


# listLength = 500
# column1 = []
# column2 = []
# for i in range(listLength):
#     column1.append(random.randint(1, 5))
#     column2.append(random.randint(1, 5))






def measure_time(func):
    # Decorator that measures and reports the time taken by a given function
    def wrap(*args, **kwargs):
        ################################################################
        # WRITE CODE HERE TO FIX 'start_time' AND 'total_time'
        start_time = time.time()
        result = func(*args, **kwargs)  # This line does not need fixing
        total_time = time.time() - start_time
        ################################################################
        print("Function '{}' took approximately {:.5f} seconds.".format(func.__name__, total_time))
        return result

    return wrap


@measure_time
def calculate_mean_manually(column):
    # Gets parameter 'column' as a list, returns its arithmetic mean
    # Calculations are done manually / "by hand" (not using external libraries)
    ###############################
    # WRITE CODE HERE TO FIX 'mean'
    sum = 0
    for i in column:
        sum = sum + i
    mean = sum / len(column)
    ###############################
    return mean


@measure_time
def calculate_sd_manually(column):
    # Gets parameter 'column' as a list, returns its standard deviation
    # Calculations are done manually / "by hand" (not using external libraries)
    #############################
    # WRITE CODE HERE TO FIX 'sd'
    sum = 0
    for i in column:
        sum = sum + i
    mean = sum / len(column)
    sum2 = 0
    for i in column:
        sum2 = sum2 + (i - mean)**2
    sd = math.sqrt(sum2 / len(column))
    #############################
    return sd



@measure_time
def calculate_linreg_manually(column1, column2):
    # Gets parameters 'column1' and 'column2' as lists, returns the intercept and slope of their OLS regression
    # Calculations are done manually / "by hand" (not using external libraries)
    ################################################
    # WRITE CODE HERE TO FIX 'intercept' AND 'slope'
    sum_y = 0
    sum_x = 0
    sum_x_2 = 0
    sum_xy = 0
    n = len(column1)
    for i in range(0,n):
        #print(i)
        sum_y = sum_y + column2[i]
        sum_x = sum_x + column1[i]
        sum_x_2 = sum_x_2 + column1[i]**2
        sum_xy = sum_xy + column1[i] * column2[i]
    
    intercept = ((sum_y*sum_x_2)-(sum_x * sum_xy))/((n*sum_x_2)-(sum_x**2))
    slope = ((n*sum_xy)-(sum_x * sum_y))/((n*sum_x_2)-(sum_x**2))
    ################################################
    return intercept, slope



@measure_time
def calculate_mean_automatically(column):
    # Gets parameter 'column' as a Pandas Series object (i.e. DataFrame column), returns its arithmetic mean
    # Calculations are done using external libraries
    ###############################
    # WRITE CODE HERE TO FIX 'mean'
    mean = np.average(column)
    ###############################
    return mean


@measure_time
def calculate_sd_automatically(column):
    # Gets parameter 'column' as a Pandas Series object (i.e. DataFrame column), returns its standard deviation
    # Calculations are done using external libraries
    #############################
    # WRITE CODE HERE TO FIX 'sd'
    sd = np.std(column)
    #############################
    return sd


@measure_time
def calculate_linreg_automatically(column1, column2):
    # Gets parameters 'column1' and 'column2' as separate Pandas DataFrame objects,
    # returns the intercept and slope of their OLS regression
    # Calculations are done using external libraries
    ################################################
    # WRITE CODE HERE TO FIX 'intercept' AND 'slope'
    reg = LinearRegression().fit(np.array(column1).reshape((-1,1)), column2)
    intercept = reg.intercept_
    slope = reg.coef_[0]
    ################################################
    return intercept, slope

# print(calculate_mean_manually(column1))
# print(calculate_sd_manually(column1))
# print(calculate_linreg_manually(column1,column2))
# print(calculate_mean_automatically(column1))
# print(calculate_sd_automatically(column1))
# print(calculate_linreg_automatically(column1,column2))


def main():
    print("Comparison of processing times between manual calculations and libraries")

    # Generates a semi-random DataFrame with two columns and between 500 000 and 2 000 000 rows
    # Some level of covariance between the two columns is randomly created
    seed = int(input('\nEnter a seed for generating the random DataFrame:\n'))
    np.random.seed(seed)
    means = np.array([np.random.randint(0, 100), np.random.randint(0, 100)])
    covariance = np.random.rand() * 2 - 1
    covariance_matrix = np.array([[1, covariance], [covariance, 1]])
    df = pd.DataFrame(np.random.multivariate_normal(means, covariance_matrix, size=np.random.randint(500000, 2000000)),
                      columns=['A', 'B'])
    print("Created a DataFrame of {} columns and {} rows.".format(df.shape[1], df.shape[0]))

    print('\nCalculating statistics manually...')
    manual_results = {}
    manual_results['mean'] = calculate_mean_manually(df['A'].tolist())
    manual_results['sd'] = calculate_sd_manually(df['A'].tolist())
    manual_results['intercept'], manual_results['slope'] = calculate_linreg_manually(df['A'].tolist(), df['B'].tolist())

    print('\nCalculating statistics using the libraries...')
    library_results = {}
    library_results['mean'] = calculate_mean_automatically(df['A'])
    library_results['sd'] = calculate_sd_automatically(df['A'])
    library_results['intercept'], library_results['slope'] = calculate_linreg_automatically(df[['A']], df[['B']])

    for key in manual_results:
        if not math.isclose(manual_results[key], library_results[key], rel_tol=0.001):
            print("\nDifferences found between the '{}' results – at least one calculation is incorrect.".format(key))
            break
    else:
        print("\nThe arithmetic mean of Column A is {:.4f}.".format(manual_results['mean']))
        print("The standard deviation of Column A is {:.4f}.".format(manual_results['sd']))
        print("The linear regression relationship between Columns A and B is roughly 'B = {:.4f} + {:.4f} × A'."
              .format(manual_results['intercept'], manual_results['slope']))


if __name__ == "__main__":
    main()
