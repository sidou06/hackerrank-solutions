# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = tuple(map(int, input().split()))  # Read x and k values from input
s = eval(input())  # Evaluate the polynomial expression with x as input
if s == k:  # Check if the evaluated result matches k
    print('True')  # Print 'True' if they match
else:
    print('False')  # Print 'False' otherwise