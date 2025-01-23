# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read the number of rooms
k = int(input())

# Read the list of room numbers
rooms = list(map(int, input().split()))

# Convert the list of rooms to a set to remove duplicates
sett = set(rooms)

# Calculate the sum of the room numbers
s1 = sum(rooms)

# Calculate the sum of the unique room numbers multiplied by k
s2 = sum(sett) * k

# Compute the missing room number and print the result
print((s2 - s1) // (k - 1))