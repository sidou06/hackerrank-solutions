# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

# Regular expression pattern to find the first occurrence of a repeated alphanumeric character
pattern = r'([a-zA-Z0-9])\1+'

# Searching the pattern in the input string
m = re.search(pattern, input())

# If a match is found, print the repeated character
if m:
    print(m.group(1))
else:
    # If no match is found, print -1
    print(-1)