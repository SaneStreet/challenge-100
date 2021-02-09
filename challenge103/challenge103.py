"""
To use the python script in Command Prompt:
Write 'python your_file_name.py'
Example: 'python challenge103.py'
"""
# Function that takes a string
def SameCase(theString):
    # Prompts the user if the given string is lower or uppercase only
    print(f"Is {theString} lower or uppercase only?")
    # checks if the string is all lowercase, or all uppercase
    if(theString.islower() or theString.isupper()):
        # if that is the case, print True
        print(theString.islower() or theString.isupper(), "\n")
    else:
        # if that is NOT the case, print False
        print(theString.islower() or theString.isupper(), "\n")

# Function calls with arguments
SameCase("michael") # returns True
SameCase("BILBO") # returns True
SameCase("Aragorn") # returns False
SameCase("SpOnGeBoB") #returns False