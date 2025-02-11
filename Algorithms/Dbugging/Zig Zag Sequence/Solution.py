def findZigZagSequence(a, n):
    # Sort the array in ascending order
    a.sort()
    
    # Find the middle index
    mid = int((n + 1) / 2) - 1
    
    # Swap the middle element with the last element
    a[mid], a[n - 1] = a[n - 1], a[mid]

    # Reverse the second half of the array to form the zig-zag pattern
    st = mid + 1
    ed = n - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    # Print the zig-zag sequence
    for i in range(n):
        if i == n - 1:
            print(a[i])  # Print last element without space
        else:
            print(a[i], end=' ')  # Print with space
    
    return

# Read number of test cases
test_cases = int(input())

# Process each test case
for cs in range(test_cases):
    n = int(input())  # Read the size of the array
    a = list(map(int, input().split()))  # Read the array elements
    findZigZagSequence(a, n)