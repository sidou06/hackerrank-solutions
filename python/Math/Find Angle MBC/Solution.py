# Enter your code here. Read input from STDIN. Print output to STDOUT

import math 

# Read the lengths of sides AB and BC
ab = int(input())
bc = int(input()) 

# Calculate the tangent of the angle
tan = ab / bc

# Calculate the angle in radians and convert it to degrees
ang = (math.atan(tan) * 180) / math.pi 

# Print the angle rounded to the nearest integer with the degree symbol
print(str(round(ang)) + "\u00B0")