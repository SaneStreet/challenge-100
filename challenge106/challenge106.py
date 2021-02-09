"""
To use the python script in Command Prompt:
Write 'python your_file_name.py'
Example: 'python challenge101.py'
"""
# function that takes a string
def AlphabetIndex(text):
    # checks if the characters from the text is in the alphabet
    # skipping any special characters (ex: ,.?!/[]{ )
    chars = "".join(c for c in text if c.isalpha())
    # en empty array to hold the numbers of given string
    numbers = []
    
    # for every character in chars (lowercased)
    # find the according ascii character and subtract 96 from it
    for character in chars.lower():
        number = ord(character) - 96
        # add the numbers to the empty array
        numbers.append(number)
    # print the numbers, with space between them
    print(*numbers, sep=' ')

# function calls with string as argument
AlphabetIndex("Wow, does that work?")
AlphabetIndex("The river stole the gods.")
AlphabetIndex("We have a lot of rain in June.")
