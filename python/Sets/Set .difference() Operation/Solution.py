# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read the size of the first set
n = int(input())

# Read the elements of the first set
listn = set(map(int, input().split()))

# Read the size of the second set
m = int(input())

# Read the elements of the second set
listm = set(map(int, input().split()))

# Compute the difference of the first set from the second and print its size
print(len(listn.difference(listm)))