if __name__ == '__main__':
    # Read an integer input for the number of elements in the list
    n = int(input())
    # Read a space-separated list of integers and map them to an integer list
    arr = map(int, input().split())
    arr = list(arr)  # Convert the map object to a list
    arr.sort()  # Sort the list in ascending order
    
    i = -2  # Start from the second-to-last element (negative indexing)
    
    # Loop to find the highest value in the list that is less than the maximum
    # Move further back in the sorted list if the current value equals the largest value
    while arr[i] == arr[-1]:
        i -= 1  # Decrement the index to find the next unique value
    
    # Print the second-largest value in the list
    print(arr[i])