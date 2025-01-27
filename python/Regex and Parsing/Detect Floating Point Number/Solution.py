# Enter your code here. Read input from STDIN. Print output to STDOUT
import re  # Import the regular expressions module

# Define the regular expression to match a valid floating-point number
reg = r'^[\+-]?(\d*)\.(\d+)$'

# Loop through the number of test cases
for _ in range(int(input())):
    # Check if the input matches the regular expression
    if re.match(reg, input()) == None:
        print(False)  # Print False if it doesn't match
    else:
        print(True)  # Print True if it matches