import textwrap  # Importing the textwrap module to wrap the string

def wrap(string, max_width):
    # Wrap the input string into lines of the specified maximum width
    # textwrap.wrap() splits the string into a list of lines, where each line has a maximum length of max_width
    return '\n'.join(textwrap.wrap(string, max_width))  # Join the lines with newlines