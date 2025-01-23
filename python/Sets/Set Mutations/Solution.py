# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read the size of the first set
n = int(input())

# Read the elements of the first set
A = set(map(int, input().split()))

# Read the number of operations
m = int(input())

# Perform each operation based on the input
for i in range(m):
    op = input().split()[0]  # Get the operation type
    s = set(map(int, input().split()))  # Read the second set for the operation
    if op == "update":
        A.update(s)  # Perform the update operation (A = A U s)
    elif op == "intersection_update":
        A.intersection_update(s)  # Perform the intersection operation (A = A ∩ s)
    elif op == "difference_update":
        A.difference_update(s)  # Perform the difference operation (A = A - s)
    else:
        A.symmetric_difference_update(s)  # Perform the symmetric difference operation (A = A Δ s)

# Print the sum of the elements in the updated set
print(sum(A))