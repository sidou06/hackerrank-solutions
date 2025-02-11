import math

def is_smart_number(num):
    # Calculate the integer square root of the number
    val = int(math.sqrt(num))
    
    # Check if squaring the integer root gives back the original number
    if num / val == val:
        return True
    return False

# Read the number of test cases
for _ in range(int(input())):
    num = int(input())  # Read the number to check
    ans = is_smart_number(num)  # Determine if it's a smart number
    if ans:
        print("YES")  # Print "YES" if it's a smart number
    else:
        print("NO")  # Print "NO" otherwise