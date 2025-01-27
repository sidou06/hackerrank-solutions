# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

# Reading the number of test cases
n = int(input()) 

# Iterating through each test case
for i in range(n):
    inp = input()  # Reading the input string
    
    # Replacing '&&' with 'and' until no more changes occur
    while True:
        a = re.sub(r' && ', ' and ', inp)
        if inp == a:
            break  # Break the loop if no changes were made
        inp = a  # Update inp with the modified string

    # Replacing '||' with 'or' until no more changes occur
    while True:
        b = re.sub(r' \|\| ', ' or ', a)
        if b == a:
            break  # Break the loop if no changes were made
        a = b  # Update a with the modified string
    
    # Printing the final modified string
    print(b)