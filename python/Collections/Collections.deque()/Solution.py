# Enter your code here. Read input from STDIN. Print output to STDOUT

# Import deque from collections module
from collections import deque

# Initialize an empty deque
d = deque()

# Read number of operations
n = int(input())

# Loop through each operation
for i in range(n):
    req = input().split()  # Read and split the input command
    if req[0] == 'pop':  # If the operation is pop, remove from the right
        d.pop()
    elif req[0] == 'popleft':  # If the operation is popleft, remove from the left
        d.popleft()
    elif req[0] == 'append':  # If the operation is append, add to the right
        d.append(req[1])
    else:  # If the operation is appendleft, add to the left
        d.appendleft(req[1])

# Print the final deque as space-separated values
print(*d)