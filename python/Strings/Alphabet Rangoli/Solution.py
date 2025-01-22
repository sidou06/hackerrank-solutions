def print_rangoli(size):
    # Define the alphabet for rangoli construction
    alp = "abcdefghijklmnopqrstuvwxyz"
    save = []  # List to store the lines of the rangoli

    # Loop to generate the top half of the rangoli
    for i in range(size - 1, -1, -1):
        let = ""  # String to store characters for each line
        # Loop to add characters from the alphabet for the current line
        for j in range(size - 1, i - 1, -1):
            let += alp[j] 
            let += "-"
        l = let[:-1]  # Remove the trailing "-" from the string
        # Add the reverse part of the string to complete the rangoli pattern
        for j in range(3, len(let) + 1):
            l += let[-j]
        # Add padding with "-" and store the line
        save.append("-" * 2 * i + l + "-" * 2 * i)
        # Print the current line of the rangoli
        print(save[-1])

    # Loop to print the bottom half of the rangoli
    for i in range(2, size + 1):
        print(save[-i]) 