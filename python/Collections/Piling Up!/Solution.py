# Enter your code here. Read input from STDIN. Print output to STDOUT

# Function to check if we can stack the blocks
def stack(blocks, l):
    # Initialize first and last block and their positions
    first = blocks[0] 
    last = blocks[-1]  
    posf = 0  # Position of first block
    posl = l - 1  # Position of last block
    cpt = 0  # Counter to track valid blocks stacked

    # First loop to check for stacking from the beginning
    while posf < l:
        if first < blocks[posf]:  # Break if block is not stackable
            break 
        first = blocks[posf]  # Update first block
        posf += 1  # Move to next position
        cpt += 1  # Increment valid counter

    # Second loop to check for stacking from the end
    while posl >= 0:
        if last < blocks[posl]:  # Break if block is not stackable
            break 
        last = blocks[posl]  # Update last block
        posl -= 1  # Move to previous position
        cpt += 1  # Increment valid counter

    # Check if the number of valid blocks stacked is greater than or equal to total blocks
    if cpt >= l:
        return True  # Blocks are stackable
    else:
        return False  # Blocks are not stackable

# Read number of test cases
t = int(input()) 

# Iterate over test cases
for i in range(t):
    # Read number of blocks
    l = int(input())
    # Read the list of blocks
    blocks = list(map(int, input().split()))
    # Check if blocks can be stacked
    res = stack(blocks, l) 
    # Print result based on the stackability of the blocks
    if res:
        print("Yes") 
    else:
        print("No")