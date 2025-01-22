def split_and_join(line):
    # Split the string into a list of words using space as the delimiter
    line = line.split(" ") 
    
    # Join the list of words with a hyphen as the delimiter
    line = "-".join(line) 
    
    # Return the resulting string
    return line