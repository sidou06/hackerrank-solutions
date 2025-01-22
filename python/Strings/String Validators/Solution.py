if __name__ == '__main__':
    # Read the input string
    s = input()
    
    # Initialize flags to track different character types
    alphan = False  # Flag to check if any alphanumeric character is found
    alph = False    # Flag to check if any alphabetic character is found
    dig = False     # Flag to check if any digit is found
    low = False     # Flag to check if any lowercase letter is found
    upp = False     # Flag to check if any uppercase letter is found
    
    # Iterate through each character in the string
    for c in s:
        # Check if the character is alphanumeric (letters or digits)
        if c.isalnum():
            alphan = True 
        # Check if the character is alphabetic (letters only)
        if c.isalpha():
            alph = True 
        # Check if the character is a digit
        if c.isdigit():
            dig = True 
        # Check if the character is lowercase
        if c.islower(): 
            low = True 
        # Check if the character is uppercase
        if c.isupper():
            upp = True 
    
    # Print the status of each flag
    print(alphan)  # Output whether any alphanumeric character exists
    print(alph)    # Output whether any alphabetic character exists
    print(dig)     # Output whether any digit exists
    print(low)     # Output whether any lowercase letter exists
    print(upp)     # Output whether any uppercase letter exists