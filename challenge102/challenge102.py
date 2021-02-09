"""
To use the python script in Command Prompt:
Write 'python your_file_name.py'
"""
# Function that takes a string
def NameShuffle(name):
    # Splits the string parameter into indexes in an arrray
    fullname = name.split(' ')
    # assigns 'first' to the value of index [0]
    first = fullname[0]
    # assigns 'last' to the value of index[1]
    last = fullname[1]
    # prints the variables 'last' and 'first'
    # with the value from the index numbers [1] and [0]
    print(f"{last} {first}")

# function calls with 1 string as argument
NameShuffle("Michael Hansen")
NameShuffle("Joe Biden")
NameShuffle("Samwise Gamgee")
NameShuffle("Obi-wan Kenobi")