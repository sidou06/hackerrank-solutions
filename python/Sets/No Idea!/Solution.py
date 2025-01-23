# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the size of the array and sets (n, m)
n, m = tuple(map(int, input().split()))

# Read the array elements
arr = list(map(int, input().split()))

# Read the elements of set A
a = set(map(int, input().split()))

# Read the elements of set B
b = set(map(int, input().split()))

# Elements that are in set A but not in set B (happiness-inducing elements)
hap = a.difference(b)

# Elements that are in set B but not in set A (sadness-inducing elements)
sad = b.difference(a)

# Initialize the counter for happiness score
cpt = 0

# Iterate through each element in the array
for i in range(n):
    # If the element is in the happiness-inducing set, increase the score
    if arr[i] in hap:
        cpt += 1
    # If the element is in the sadness-inducing set, decrease the score
    elif arr[i] in sad:
        cpt -= 1

# Print the final happiness score
print(cpt)