if __name__ == '__main__':
    # Read an integer input representing the number of elements in the tuple
    n = int(input())
    
    # Read space-separated integers, map them to integers, and convert to a tuple
    integer_list = tuple(map(int, input().split()))
    
    # Compute and print the hash of the tuple
    print(hash(integer_list))