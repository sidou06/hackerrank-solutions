if __name__ == '__main__':
    lis = []  # Initialize an empty list to store [name, score] pairs
    
    # Read the number of students and their respective names and scores
    for _ in range(int(input())):
        name = input()  # Read the name of the student
        score = float(input())  # Read the score of the student
        lis.append([name, score])  # Append the [name, score] pair to the list
    
    # Sort the list based on the score (second element of each pair)
    lis.sort(key=lambda x: x[1])
    
    i = 1  # Start from the second element in the sorted list
    
    # Find the index of the first score that is higher than the minimum score
    while lis[i][1] == lis[0][1]:  # Compare with the minimum score (first element)
        i += 1  # Increment the index until a higher score is found
    
    j = i  # Set j to the index of the second lowest score
    
    names = []  # Initialize a list to store names with the second lowest score
    
    # Collect all names with the second lowest score
    while j < len(lis) and lis[j][1] == lis[i][1]:
        names.append(lis[j][0])  # Append the name to the list
        j += 1  # Increment the index
    
    names.sort()  # Sort the names alphabetically
    
    # Print each name on a new line
    for name in names:
        print(name)