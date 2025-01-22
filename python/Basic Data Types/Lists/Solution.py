if __name__ == '__main__':
    N = int(input())  # Read the number of commands
    lis = []  # Initialize an empty list
    
    for _ in range(N):
        act = input().split()  # Split the command into a list of strings
        
        # Handle the 'insert' command
        if act[0] == "insert":
            lis.append(0)  # Temporarily extend the list to accommodate insertion
            st = int(act[1]) + 1  # Compute the insertion index plus one
            lis[st:] = lis[int(act[1]):-1]  # Shift elements to the right
            lis[int(act[1])] = int(act[2])  # Insert the specified value
        
        # Handle the 'print' command
        elif act[0] == "print":
            print(lis)  # Print the current state of the list
        
        # Handle the 'remove' command
        elif act[0] == "remove":
            lis.pop(lis.index(int(act[1])))  # Remove the first occurrence of the specified value
        
        # Handle the 'append' command
        elif act[0] == "append":
            lis.append(int(act[1]))  # Append the specified value to the end of the list
        
        # Handle the 'sort' command
        elif act[0] == "sort":
            lis.sort()  # Sort the list in ascending order
        
        # Handle the 'pop' command
        elif act[0] == "pop":
            lis.pop(-1)  # Remove the last element from the list
        
        # Handle the 'reverse' command
        else:
            lis.reverse()  # Reverse the list