def is_leap(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If the year is divisible by 100, further check if it's divisible by 400
        if year % 100 == 0:
            # If the year is divisible by 400, it's a leap year
            if year % 400 == 0:
                return True 
            # If divisible by 100 but not by 400, it's not a leap year
            return False 
        # If divisible by 4 but not 100, it's a leap year
        return True 
    # If not divisible by 4, it's not a leap year
    return False 
    # Write your logic here
    
    return leap  # This line is redundant, as the function will already return before it reaches here.
