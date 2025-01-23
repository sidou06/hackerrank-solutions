# Enter your code here. Read input from STDIN. Print output to STDOUT

# Iterate over the range from 1 to the input number (exclusive)
for i in range(1, int(input())):
    # Calculate and print the value for the current iteration
    print(i * (((10 ** i) - 1) // 9))