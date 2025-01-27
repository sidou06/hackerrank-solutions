def fun(s):
    # Return True if s is a valid email, else return False
    email_pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'  # Regular expression for validating email
    return re.match(email_pattern, s)  # Check if the string matches the pattern

import re  # Import the re module for regular expression operations