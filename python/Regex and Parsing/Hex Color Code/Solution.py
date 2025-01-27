# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

# Regular expression to match valid hex color codes
reg = r'#[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?[^a-fA-F0-9]'

opened = False  # Flag to track if we're inside the curly braces

for i in range(int(input())):  # Loop over each input line
    s = input()  # Read the input string
    if "{" in s:  # Check if the line contains an opening brace
        opened = True 
    elif s == "}":  # Check if the line contains a closing brace
        opened = False 
    elif opened:  # If inside braces, check for valid hex colors
        for ele in re.findall(reg, s):  # Find all hex color codes
            print(ele[:-1])  # Remove the trailing character and print the result