# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
import email.utils 

# Regular expression to match a valid email format
reg = r'^[a-zA-Z][a-zA-Z0-9_\-\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

for _ in range(int(input())):
    name, em = input().split()  # Split input into name and email
    em = em[1:-1]  # Remove the surrounding angle brackets from email
    if re.match(reg, em):  # Check if the email matches the regular expression
        print(email.utils.formataddr((name, em)))  # Print the formatted email address