"""
To use the python script in Command Prompt:
Write 'python your_file_name.py'
Example: 'python challenge101.py'
"""
# function that needs a string
def IsIsogram(checkWord):
        # assigns the value of checkWord to 'word'
        word = checkWord
        # makes an array for the letters
        letters = []
        # a for loop, that checks every letter in 'word'
        for letter in word:
            # if the letter is in the alphabet do something
            if letter.isalpha():
                if letter in letters:
                    # if the letter IS NOT in the alphabet
                    return False
                # put the letter back to the end of the list
                letters.append(letter)
        # if the letter IS in the alphabet
        return True

# function calls with arguments
print("Is the words isograms?")
print(IsIsogram("isogram")) # True
print(IsIsogram("Password")) # False
print(IsIsogram("Alabama")) #Very False
print(IsIsogram("Mr. Bean")) # Actually True