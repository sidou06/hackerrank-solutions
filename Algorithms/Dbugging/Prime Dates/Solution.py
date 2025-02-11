import re

# Array to store the number of days in each month
month = []

# Function to update February's days based on leap year rules
def updateLeapYear(year):
    if year % 400 == 0:
        month[2] = 29
    elif year % 100 == 0:
        month[2] = 28
    elif year % 4 == 0:
        month[2] = 29
    else:
        month[2] = 28

# Function to initialize the month array with days for each month
def storeMonth():
    month[1] = 31
    month[2] = 28
    month[3] = 31
    month[4] = 30
    month[5] = 31
    month[6] = 30
    month[7] = 31
    month[8] = 31
    month[9] = 30
    month[10] = 31
    month[11] = 30
    month[12] = 31

# Function to count prime dates in the given range
def findPrimeDates(d1, m1, y1, d2, m2, y2):
    storeMonth()  # Initialize month array
    result = 0  # Counter for prime dates

    while True:
        # Construct the date number in the format DDMMYYYY
        x = d1
        x = x * 100 + m1
        x = x * 10000 + y1

        # Check divisibility by 4 or 7
        if x % 4 == 0 or x % 7 == 0:
            result += 1

        # Stop if the end date is reached
        if d1 == d2 and m1 == m2 and y1 == y2:
            break

        # Update leap year settings for February
        updateLeapYear(y1)

        # Increment the day
        d1 += 1

        # Handle month overflow
        if d1 > month[m1]:
            m1 += 1
            d1 = 1

            # Handle year overflow
            if m1 > 12:
                y1 += 1
                m1 = 1

    return result

# Initialize the month array with 31 days (temporary values)
for i in range(1, 15):
    month.append(31)

# Read input and split it into date components
line = input()
date = re.split('-| ', line)
d1 = int(date[0])
m1 = int(date[1])
y1 = int(date[2])
d2 = int(date[3])
m2 = int(date[4])
y2 = int(date[5])

# Compute and print the result
result = findPrimeDates(d1, m1, y1, d2, m2, y2)
print(result)