def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    nb = n // k  # Calculate the number of substrings
    
    # Loop through each substring of length k
    for i in range(nb):
        st = i * k  # Starting index of the substring
        tmp = string[st:st + k]  # Extract the substring
        re = ""  # String to store the result without duplicates
        exist = []  # List to track characters already added
        
        # Loop through each character in the substring
        for j in range(k):
            # If the character is not in the 'exist' list, add it to 're'
            if tmp[j] not in exist:
                exist.append(tmp[j])
                re += tmp[j]
            j += 1
        
        # Print the result for the current substring
        print(re)