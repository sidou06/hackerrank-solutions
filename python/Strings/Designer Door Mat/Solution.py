# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read the input to get the size n
n = int(input().split()[0])

# Calculate the maximum width of the pattern
m = 3 * n 

# Print the top part of the pattern (the first half of the design)
for i in range(n // 2):
    # Print the left padding, the ".|." patterns, and the right padding
    # The number of ".|." increases as we go down the rows
    # The padding on both sides decreases as we go down the rows
    print("-" * ((3 * (n // 2)) - 3 * i) + ".|." * (2 * i + 1) + "-" * ((3 * (n // 2)) - 3 * i))

# Print the center "WELCOME" line
# Calculate the padding for the left and right sides of "WELCOME"
print("-" * ((3 * n - 7) // 2) + "WELCOME" + "-" * ((3 * n - 7) // 2))

# Print the bottom part of the pattern (the second half of the design)
# This part is a mirror of the top part
for i in range(n // 2 - 1, -1, -1):
    # Print the left padding, the ".|." patterns, and the right padding
    # The number of ".|." decreases as we go up the rows
    # The padding on both sides increases as we go up the rows
    print("-" * ((3 * (n // 2)) - 3 * i) + ".|." * (2 * i + 1) + "-" * ((3 * (n // 2)) - 3 * i))