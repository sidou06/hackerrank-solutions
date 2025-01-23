# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read the size of the first set
m = int(input().rstrip())

# Read the elements of the first set
set1 = set(list(map(int, input().rstrip().split())))

# Read the size of the second set
n = int(input().rstrip())

# Read the elements of the second set
set2 = set(list(map(int, input().rstrip().split())))

# Compute the symmetric difference (elements in either set but not both)
s = set1.union(set2).difference(set1.intersection(set2))

# Convert the result to a sorted list
s = list(s)
s.sort()

# Print each element of the sorted symmetric difference
for ele in s:
    print(ele)