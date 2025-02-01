#!/bin/python3

import math  # Importing math module for mathematical operations
import os  # Importing os module to interact with the operating system
import random  # Importing random module for generating random numbers (though not used here)
import re  # Importing re module for regular expressions (though not used here)
import sys  # Importing sys module for system-specific parameters and functions

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n - total number of astronauts
#  2. 2D_INTEGER_ARRAY astronaut - list of pairs of astronauts that are connected

# Helper function to remove a country from the list of countries
def suppprimer(countries, i):
    return(countries[:i] + countries[i + 1:])  # Remove the i-th country from the countries list

def journeyToMoon(n, astronaut):
    # List to store connected countries (groups of astronauts connected by pairs)
    countries = []

    # Loop through each astronaut pair to form connections
    for pair in astronaut:
        country1 = False  # Flag to check if the first astronaut is already in a country
        country2 = False  # Flag to check if the second astronaut is already in a country

        # Loop through the existing countries to see if either astronaut is already in a country
        for i in range(len(countries)):
            if pair[0] in countries[i]:  # If the first astronaut is in a country
                country1 = True  # Mark the first astronaut as found in a country
                a = countries[i]  # Save the set of astronauts in that country
                ind1 = i  # Save the index of the first country
            if pair[1] in countries[i]:  # If the second astronaut is in a country
                country2 = True  # Mark the second astronaut as found in a country
                b = countries[i]  # Save the set of astronauts in that country
                ind2 = i  # Save the index of the second country
            if country1 and country2:  # If both astronauts are found, stop the loop
                break

        # If neither astronaut is in any country, create a new country with the current pair
        if not country1 and not country2:
            countries.append(set([pair[0], pair[1]]))  # Create a new country (set) with the pair
        # If only the second astronaut is not in a country, add them to the first country's set
        elif not country2:
            a.add(pair[1])  # Add the second astronaut to the first country's set
            countries[ind1] = a  # Update the first country's set in the countries list
        # If only the first astronaut is not in a country, add them to the second country's set
        elif not country1:
            b.add(pair[0])  # Add the first astronaut to the second country's set
            countries[ind2] = b  # Update the second country's set in the countries list
        # If both astronauts are in different countries, merge the two countries into one
        elif ind1 != ind2:
            a.update(b)  # Merge the second country's set into the first country's set
            countries[ind1] = a  # Update the first country's set in the countries list
            countries = suppprimer(countries, ind2)  # Remove the second country from the list

    # Create a list to store the sizes of each country (number of astronauts in each group)
    l = []
    s = 0  # Variable to track the total number of astronauts in all countries

    # Loop through the countries and add their sizes to the list l
    for ele in countries:
        l.append(len(ele))  # Append the size of each country (number of astronauts)
        s += len(ele)  # Add the size to the total count of astronauts

    # Add individual astronauts who are not in any country to the list (each counted as a single astronaut)
    for i in range(n - s):
        l.append(1)  # Add 1 for each astronaut who is alone and not in any country

    # Variable to calculate the total number of possible pairs
    tot = 0
    mul = n  # Start with the total number of astronauts

    # Calculate the total number of valid pairs by considering each country
    for nb in l:
        mul = mul - nb  # Subtract the size of the current country from the remaining astronauts
        tot += nb * mul  # Multiply the size of the current country by the remaining astronauts and add to total

    return(tot)  # Return the total number of valid astronaut pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open the output file

    # Input for number of astronauts and pairs
    first_multiple_input = input().rstrip().split()  # Read the first input line and split by space

    n = int(first_multiple_input[0])  # Total number of astronauts
    p = int(first_multiple_input[1])  # Number of astronaut pairs

    astronaut = []  # List to store pairs of astronauts

    # Input the pairs of astronauts
    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))  # Read each pair of astronauts

    result = journeyToMoon(n, astronaut)  # Call the function to get the result

    fptr.write(str(result) + '\n')  # Write the result to the output file

    fptr.close()  # Close the output file