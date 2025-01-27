import re

# Define regular expression for valid UID
reg = r'^[a-zA-Z0-9]{10}$'

# Iterate over the number of test cases
for _ in range(int(input())):
    uid = input() 
    
    # Check if UID matches length, regex, and uniqueness condition
    if len(uid) == 10 and re.match(reg, uid) and len(set(uid)) == 10:
        u = 0  # Counter for uppercase letters
        d = 0  # Counter for digits
        
        # Iterate over each character in UID
        for c in uid:
            # Count uppercase and digit characters
            if c.isupper():
                u += 1
            elif c.isdigit():
                d += 1
        
        # Check if there are at least 2 uppercase letters and 3 digits
        if u > 1 and d > 2:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")