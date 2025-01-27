import re

# Function to check the validity of a card
def card_check(card):
    # Regular expression to match the card pattern
    card_regex = r'^(?!.*(\d)(-?\1){3})[456]\d{3}(-?\d{4}){3}$'
    
    # Check if card matches the regex
    if re.match(card_regex, card):
        print("Valid") 
    else:
        print("Invalid")

# Read number of test cases
n = int(input())

# Iterate over the test cases
for u in range(n):
    card = input()  # Input the card number
    card_check(card)  # Check if the card is valid