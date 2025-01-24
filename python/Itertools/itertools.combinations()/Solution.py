# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations as co 

# Read and process the input
s = input().split()
word = s[0]  # Input word
k = int(s[1])  # Maximum length of combinations
w = sorted(word)  # Sort the word alphabetically

# Generate and print combinations of increasing lengths from 1 to k
for i in range(1, k + 1):
    l = list(co(w, i))  # Generate combinations of length i
    for ele in l:
        f = ''.join([str(let) for let in ele])  # Join characters to form a string
        print(f)  # Print the combination