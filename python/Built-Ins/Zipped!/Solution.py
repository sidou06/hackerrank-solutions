# Enter your code here. Read input from STDIN. Print output to STDOUT
liste = []  # Initialize an empty list to store the input data
x, n = tuple(map(int, input().split()))  # Read x and n values from input

# Read n lists of floats and store them in 'liste'
for i in range(n):
    liste.append(list(map(float, input().split())))

# Transpose the matrix using zip and unpacking
r = list(zip(*liste))

# Calculate the average for each column and print the result
for ele in r: 
    print(sum(ele) / n)