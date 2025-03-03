import sys

def go():
    # Read input values n, k, and p from standard input
    n, k, p = map(int, sys.stdin.readline().split())

    # Initialize values for computation
    A = n + 1
    B = k + 1
    res = 1  # Result accumulator

    # Compute factorial modulo p for values from 0 to p-1
    f = [1]  # List to store factorial values modulo p
    for i in range(1, p):
        f.append(f[-1] * i % p)  # Compute factorial modulo p iteratively

    # Apply Lucas' theorem to compute nCk % p
    while A or B:
        a, b = A % p, B % p  # Extract last digits in base p
        A //= p  # Reduce A by factor of p
        B //= p  # Reduce B by factor of p

        # If a < b, result is 0 because nCk is not possible
        if a < b:
            return 0

        # Compute binomial coefficient modulo p using modular inverse
        res *= f[a] * pow(f[b] * f[a - b] % p, p - 2, p)
        res %= p  # Apply modulo operation

    return res  # Return final computed value

# Read number of test cases
for _ in range(int(sys.stdin.readline())):
    print(go())  # Execute function for each test case and print result