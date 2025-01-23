# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read the two integers a and b
a = int(input())
b = int(input())

# Print the quotient of a divided by b using floor division
print(a // b) 

# Print the remainder of a divided by b
print(a % b) 

# Print the result of divmod(a, b), which returns a tuple (quotient, remainder)
print(divmod(a, b))