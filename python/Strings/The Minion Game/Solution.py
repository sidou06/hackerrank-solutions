def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    l = len(string)
    cptv = 0  # Count of substrings starting with a vowel
    cptc = 0  # Count of substrings starting with a consonant
    
    # Loop through each character in the string
    for i in range(l):
        # If the character is a vowel, add the count of substrings starting with this vowel
        if string[i] in vowels:
            cptv += l - i
        # If the character is not a vowel, add the count of substrings starting with this consonant
        else:
            cptc += l - i
    
    # Compare counts and print the result
    if cptc > cptv:
        print("Stuart " + str(cptc))
    elif cptv > cptc:
        print("Kevin "+ str(cptv))
    else:
        print("Draw")