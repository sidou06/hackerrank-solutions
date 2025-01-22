# Complete the solve function below.
def solve(s):
    # Loop through each character in the string
    for i in range(len(s)):
        # If it's the first character, capitalize it
        if i == 0:
            s = s[0].upper() + s[1:]
        # If the previous character is a space, capitalize the current character
        elif s[i-1] == " ":
            s = s[:i] + s[i].upper() + s[i + 1:]
    return s