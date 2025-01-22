thickness = int(input()) #This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    # The cone is created by adjusting spaces with rjust and ljust
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    # The pillars are created by centering the "H" blocks
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    # The middle belt is a large centered string of "H"s
    print((c*thickness*5).center(thickness*6))    

# Bottom Pillars
for i in range(thickness+1):
    # The bottom pillars are similar to the top pillars, with centered "H" blocks
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))    

# Bottom Cone
for i in range(thickness):
    # The bottom cone is the inverse of the top cone, with rjust and ljust used for alignment
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))