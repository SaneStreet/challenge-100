"""
To use the python script in Command Prompt:
Write 'python your_file_name.py'
Example: 'python challenge101.py'
"""
# imports the 'month_name' functionality from the calendar module
from calendar import month_name
# function with int as parameter
def MonthName(number):
    # variable holding the name of the month from 'number'
    monthName = month_name[number]

    # if number is less than 1
    if(number < 1):
        # prompt the user with a message
        print("Number is below 1. Must be between 1 - 12.")
    # else if number is more than 12
    elif(number > 12):
        # prompt the user with a message
        print("Number is above 12. Must be between 1 - 12.")
    # if everything above is False
    else:
        # print the name of the month
        print(monthName)

# function calls with arguments (must be a number between 1 - 12)
MonthName(1)
MonthName(4)
MonthName(12)