# Enter your code here. Read input from STDIN. Print output to STDOUT

n, liste = input(), list(map(int, input().split()))  # Read the input size and list of integers
# Check if all numbers are non-negative and at least one number is a palindrome
print(all(map(lambda x: x >= 0, liste)) and any(map(lambda x: str(x) == str(x)[::-1], liste)))