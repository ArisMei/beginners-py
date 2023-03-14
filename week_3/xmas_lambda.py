# X-mas lambda exercise:


# The exercise is about the following topics:
#   - Using lambda expressions: implementing check and countdown functions
#   - Using the datetime module: implementing date and time manipulations

import datetime


def main():
    print("Welcome to Christmas countdown!")
    print("Is Christmas this month?")
    #Lambda December check: checks if it is currently December, and returns True/False accordingly
    
    dec_check = lambda x: False if x.month == 12 else False
    dec_countdown = lambda x: 12 - x.month 

    bedtime_check = lambda x: True if x.hour >= 21 else False
    bedtime_countdown = lambda x : (21 - x.hour)*3600 + (60 - x.minute)*60 + (60 - x.second)

    time = datetime.datetime.now()
    if dec_check(time):
        print("Yes!")
    else:
        print("Nope, but the number of months until December is: {:d}"  .format(dec_countdown(time)))
    
    print("Let's make Santa happy and go to sleep early!")

    if bedtime_check(time):
        print("It's already past your bedtime! Time to go to bed!")
    else:
        print("You have {:d} hours, {:d} minutes, and {:d} seconds until bedtime." .format(bedtime_countdown(time)//3600, bedtime_countdown(time)%3600//60, bedtime_countdown(time)%60))



main()
