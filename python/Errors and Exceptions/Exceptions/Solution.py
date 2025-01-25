# Read the number of test cases
t = int(input().rstrip())

# Iterate through each test case
for i in range(t):
    # Read the input and split it into two values
    ab = input().rstrip().split()
    try:
        # Attempt integer division and print the result
        print(int(ab[0]) // int(ab[1]))
    except ValueError as e:
        # Handle value error (e.g., invalid integers)
        print("Error Code:", e)
    except ZeroDivisionError as e:
        # Handle division by zero error
        print("Error Code:", e)