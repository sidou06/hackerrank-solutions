# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

# Read input date as a list of integers
l = list(map(int, input().split()))
m, d, y = l[0], l[1], l[2]

# Get the weekday of the given date
day = calendar.weekday(y, m, d)

# Print the name of the weekday in uppercase
print(calendar.day_name[day].upper())