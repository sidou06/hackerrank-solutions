# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read the number of test cases
t = int(input())

# Iterate over each test case
for i in range(t):
    # Read the size of the first set
    a = int(input())
    
    # Read the elements of the first set
    s1 = set(map(int, input().split()))
    
    # Read the size of the second set
    b = int(input())
    
    # Read the elements of the second set
    s2 = set(map(int, input().split()))
    
    # Find the intersection of the two sets
    inter = s1.intersection(s2)
    
    # Check if the intersection has the same number of elements as the first set
    if len(inter) == a:
        print("True")
    else:
        print("False")