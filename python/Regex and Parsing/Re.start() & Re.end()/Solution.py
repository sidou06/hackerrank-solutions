# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

# Reading input string and pattern
s, k = input(), input() 

# Finding overlapping matches using lookahead
m = re.finditer(f'(?=({k}))', s) 
done = False 

# Iterating through matches
for ele in m:
    st = ele.start(1)  # Start position of the match
    en = ele.end(1) - 1  # End position of the match
    print((st, en))  # Print the start and end positions as a tuple
    done = True 

# If no matches were found, print (-1, -1)
if not done:
    print("(-1, -1)")