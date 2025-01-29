def is_vowel(letter):
    # Check if the letter is a vowel
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    # Loop through each word in the words list
    for word in words:
        num_vowels = 0
        # Count the vowels in the current word
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        # Add points based on the number of vowels
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score