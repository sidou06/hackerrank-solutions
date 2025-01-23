# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read the size of the first set
n = int(input())

# Read the elements of the first set
listn = set(map(int, input().split()))

# Read the size of the second set
m = int(input())

# Read the elements of the second set
listm = set(map(int, input().split()))

# Compute the symmetric difference of the two sets and print its size
print(len(listn.symmetric_difference(listm)))