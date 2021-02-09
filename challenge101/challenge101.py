"""
To use the python script in Command Prompt:
Write 'python your_file_name.py'
"""

# Four different arrays
numbers = [5, 10, 50, 75, 250]
moreNumbers = [540, 41, 78, 91, 2]
onlyTwoNumbers = [0, 1]
onlyOneNumber = [5]

# Function that finds the minimum and maximum numbers from an array
def FindMinMax(arrayOfNumbers):
    # Uses the built-in function min() to find the lowest number
    minimumNumber = min(arrayOfNumbers)
    # Uses the built-in function max() to find the largest number
    maximumNumber = max(arrayOfNumbers)
    # Prints a message with a normal string
    print("From the list specified:")
    # Prints the minimum and maximum number using a formatted (f) string
    print(f"Minimum is {minimumNumber}")
    print(f"Maximum is {maximumNumber}\n")

# Calls the functions with arguments
FindMinMax(numbers)
FindMinMax(moreNumbers)
FindMinMax(onlyTwoNumbers)
FindMinMax(onlyOneNumber)