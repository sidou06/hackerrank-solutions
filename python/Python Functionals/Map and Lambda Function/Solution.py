cube = lambda x: x ** 3  # Lambda function to calculate the cube of a number

def fibonacci(n):
    # Return a list of Fibonacci numbers
    if n == 0:  # If n is 0, return an empty list
        return []
    elif n == 1:  # If n is 1, return a list containing only 0
        return [0]
    else:
        r = [0, 1]  # Initialize the Fibonacci series with the first two numbers
        for i in range(2, n):  # Generate the rest of the series up to n
            r.append(r[i - 1] + r[i - 2])  # Add the sum of the last two numbers to the list
        return r