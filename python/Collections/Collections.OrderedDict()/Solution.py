# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

# Initialize an ordered dictionary to store item names and their prices
d = OrderedDict()

# Input number of transactions
n = int(input().rstrip())

# Process each transaction
for i in range(n):
    it = input().rstrip().split()  # Split the input into list
    price = int(it[-1])  # Extract the last element as the price
    name = it[0]  # The first element is the item's name
    i = 1
    # If the item name has multiple words, combine them
    while i < len(it) - 1:
        name += " "
        name += it[i]
        i += 1
    # Add the price to the corresponding item in the ordered dictionary
    if name not in d:
        d[name] = price  # If the item is not yet in dictionary, add it
    else:
        d[name] += price  # If the item is already in dictionary, add to its price

# Print the item names and their corresponding total prices
for item in d:
    print(item, d[item])