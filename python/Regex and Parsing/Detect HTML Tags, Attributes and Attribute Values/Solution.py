from html.parser import HTMLParser

# Define custom HTMLParser class inheriting from HTMLParser
class myhtmlparser(HTMLParser):
    # Handle the start tag and its attributes
    def handle_starttag(self, tag, attrs):
        # Print the tag name
        print(tag)
        # Iterate through the attributes and print them
        for attr in attrs:
            a, v = attr
            print("->", a, ">", v)

# Initialize an empty string to store the input HTML content
html = ""

# Read input lines and concatenate them into the string
for _ in range(int(input())):
    html += input()

# Create an instance of the custom parser
parser = myhtmlparser()

# Feed the concatenated HTML content to the parser
parser.feed(html)

# Close the parser after processing
parser.close()