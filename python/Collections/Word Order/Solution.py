# Enter your code here. Read input from STDIN. Print output to STDOUT

# Input number of words
n = int(input())

# Initialize an empty dictionary to store word frequencies
dic = {}

# Loop through each input word
for i in range(n):
    word = input()
    if word in dic:
        dic[word] += 1  # If word already exists, increment its frequency
    else:
        dic[word] = 1  # If word doesn't exist, add it with frequency 1

# Print the number of distinct words (keys in the dictionary)
print(len(dic))

# Print the frequencies of the words (values in the dictionary)
print(" ".join(str(ele) for ele in dic.values()))