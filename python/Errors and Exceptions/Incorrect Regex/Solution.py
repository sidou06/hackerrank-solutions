# Import the regular expression module
import re 

# Read the number of test cases
n = int(input())

# Iterate through each test case
for i in range(n):
    # Read the regular expression
    reg = input()
    try:
        # Try to compile the regular expression
        re.compile(reg) 
        print("True")
    except re.error:
        # Handle invalid regular expressions
        print("False")