# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

# Regular expression to match vowels occurring between consonants
r = r'(?<=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])[aeouiAEOUI]{2,}(?=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])'

# Finding all matches in the input string
l = re.findall(r, input())

# If no matches are found, print -1
if len(l) == 0:
    print(-1)
else:
    # Print each match on a new line
    print(*l, sep="\n")