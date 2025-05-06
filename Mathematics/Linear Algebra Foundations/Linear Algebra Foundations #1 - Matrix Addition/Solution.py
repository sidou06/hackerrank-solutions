# Enter your code here. Read input from STDIN. Print output to STDOUT

# Define matrix a
a = [[1,2,3],[2,3,4],[1,1,1]]

# Define matrix b
b = [[4,5,6],[7,8,9],[4,5,7]]

# Add corresponding elements of matrices a and b
c = [[a[i][j] + b[i][j] for j in range (3)] for i in range(3)]

# Print each element of the resulting matrix c
for i in range(3):
    for j in range(3):
        print(c[i][j])
















