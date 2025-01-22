def count_substring(string, sub_string):
    # Initialize the count to 0
    count = 0
    
    # Loop through the string, ensuring we don't go beyond the substring's length
    for i in range(len(string) - len(sub_string) + 1):
        # Check if the substring starting at the current index matches the sub_string
        if string[i:i + len(sub_string)] == sub_string:
            # Increment the count if a match is found
            count += 1
    
    # Return the total count of matches
    return count