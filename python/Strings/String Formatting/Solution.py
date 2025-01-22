def print_formatted(number):
    # Calculate the length of the binary representation of the number, excluding the "0b" prefix
    p = len(bin(number)) - 2
    
    # Loop through each number from 1 to the given number
    for n in range(1, number + 1):
        # Get the hexadecimal representation of the number, remove the "0x" prefix, and convert to uppercase
        h = hex(n)[2:].upper() 
        # Get the octal representation of the number, remove the "0o" prefix
        o = oct(n)[2:]
        # Get the binary representation of the number, remove the "0b" prefix
        b = bin(n)[2:]
        
        # Print the number, octal, hexadecimal, and binary values, right-justified to the same width
        print(str(n).rjust(p) + " " + o.rjust(p) + " " + h.rjust(p) + " " + b.rjust(p))