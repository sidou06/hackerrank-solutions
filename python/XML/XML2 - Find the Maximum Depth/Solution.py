maxdepth = 0 

def depth(elem, level):
    global maxdepth 
    # Update maxdepth if the current level exceeds it
    if level > maxdepth:
        maxdepth = level
    # Traverse through all child elements recursively
    for child in elem:
        depth(child, level + 1)