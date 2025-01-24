# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

# Initialize total profit
total = 0

# Input the number of shoes available
x = int(input().rstrip())

# Input the sizes of the shoes and create a counter for shoe inventory
mylist = [int(nb) for nb in input().rstrip().split()]
m = Counter(mylist)

# Input the number of customers
t = int(input().rstrip())

# Initialize profit variable
p = 0

# Process each customer's request
for i in range(t):
    li = [int(nb) for nb in input().rstrip().split()]  # Read customer's requested size and price
    if m[li[0]] > 0:  # Check if the requested size is in stock
        m[li[0]] -= 1  # Reduce the stock of the requested size
        p += li[1]  # Add the price to the profit

# Output the total profit
print(p)