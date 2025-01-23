# Enter your code here. Read input from STDIN. Print output to STDOUT

# Iterate over the range from 1 to the input number
for i in range(1, int(input()) + 1):
    # Calculate the square of the repeated digit number (1, 11, 111, 1111, ...)
    print(((pow(10, i) - 1) // 9) ** 2)
