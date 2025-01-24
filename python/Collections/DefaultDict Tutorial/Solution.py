# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

# Input n and m
a = list(map(int, input().rstrip().split()))
n, m = a[0], a[1]

# Initialize a defaultdict to store group A's words and their indices
d = defaultdict(list)

# Input words for group A and store their indices
for i in range(n):
    d[input().rstrip()].append(i + 1)

# Input words for group B and check their indices in group A
for i in range(m):
    let = d[input().rstrip()]  # Get the list of indices for the word
    if let == []:  # If the word is not in group A
        print(-1)
    else:  # If the word is in group A, print its indices
        for k in let:
            print(k, end=' ')
        print('')