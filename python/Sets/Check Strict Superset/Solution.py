# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read the initial set
s = set(map(int, input().split()))

# Read the number of sets to compare
n = int(input())

# Initialize the result as True
re = True

# Iterate through each set
for i in range(n):
    # Read the current set
    s1 = set(map(int, input().split()))
    
    # Check if the difference is non-empty or if s1 is larger than s
    if s1.difference(s) != set() or len(s) <= len(s1):
        re = False  # Set the result to False if condition is met
        break

# Print the result
print(re)