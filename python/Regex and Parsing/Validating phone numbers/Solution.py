# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
reg = r'^[789](\d){9}$'  # Regular expression to match a 10-digit phone number starting with 7, 8, or 9
for _ in range(int(input())):
    if re.match(reg, input()):  # Check if the input matches the phone number pattern
        print("YES")  # If match found, print "YES"
    else:
        print("NO")  # If no match found, print "NO"