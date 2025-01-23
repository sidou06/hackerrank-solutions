# Read the size of the set
n = int(input())

# Read the elements of the set
s = set(map(int, input().split()))

# Read the number of commands to execute
N = int(input())

# Execute each command
for i in range(N):
    # Parse the command and its arguments
    line = input().split()
    # Perform the corresponding operation on the set
    if line[0] == "pop":
        s.pop()
    elif line[0] == "remove":
        s.remove(int(line[1]))
    else:
        s.discard(int(line[1]))

# Print the sum of the elements in the set
print(sum(s))