def mutate_string(string, position, character):
    # Take the substring from the start up to the given position (not inclusive)
    # Add the new character at the specified position
    # Append the remaining part of the string from the position + 1 onward
    return string[:position] + character + string[position + 1:]