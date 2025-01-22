if __name__ == '__main__':
    # Read an integer input for the range of x (0 to x inclusive)
    x = int(input())
    # Read an integer input for the range of y (0 to y inclusive)
    y = int(input())
    # Read an integer input for the range of z (0 to z inclusive)
    z = int(input())
    # Read an integer input representing the condition for exclusion
    n = int(input())
    
    # Generate a list of lists [i, j, k] where:
    # - i ranges from 0 to x
    # - j ranges from 0 to y
    # - k ranges from 0 to z
    # - The sum of i, j, and k is not equal to n
    li = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    
    # Print the resulting list
    print(li)