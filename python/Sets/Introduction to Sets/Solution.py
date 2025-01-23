def average(array):
    # Convert the input array to a set to remove duplicates, then back to a list
    a = list(set(array))
    # Calculate and return the average of the unique elements
    return sum(a) / len(a)