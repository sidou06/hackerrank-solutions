if __name__ == '__main__':
    # Read an integer input which determines the number of iterations
    n = int(input())
    
    # Loop through numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Print the current number i without a newline (end='' prevents the default line break)
        print(i, end = '')