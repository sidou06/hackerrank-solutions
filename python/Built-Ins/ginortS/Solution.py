# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input()  # Read the input string

# Separate and sort characters based on their categories
lower = sorted("".join(c for c in s if c.islower()))  # Sort lowercase letters
upper = sorted("".join(c for c in s if c.isupper()))  # Sort uppercase letters
digit = sorted("".join(c for c in s if c.isdigit() and int(c) % 2 == 1))  # Sort odd digits
digit2 = sorted("".join(c for c in s if c.isdigit() and int(c) % 2 == 0))  # Sort even digits

# Concatenate the sorted results
l = "".join(a for a in lower)
u = "".join(a for a in upper)
d = "".join(a for a in digit)
d2 = "".join(a for a in digit2)

# Print the final result
print(l + u + d + d2)