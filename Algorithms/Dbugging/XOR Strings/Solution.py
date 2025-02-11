def strings_xor(s, t):
    # Initialize result string
    res = ""
    
    # Iterate through each character in the strings
    for i in range(len(s)):
        if s[i] == t[i]:  # If characters are the same, append '0'
            res += '0'
        else:  # If characters are different, append '1'
            res += '1'
    
    return res

# Read input strings
s = input()
t = input()

# Print the XOR result of the two strings
print(strings_xor(s, t))