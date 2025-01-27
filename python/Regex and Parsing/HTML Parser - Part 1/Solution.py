# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser 

# Define custom HTMLParser class inheriting from HTMLParser
class myhtmlparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # Handle start tag
        print("Start :", tag)
        for (a, v) in attrs:
            # Print attributes of the start tag
            print("->", a, ">", v)

    def handle_endtag(self, tag):
        # Handle end tag
        print("End   :", tag)

    def handle_comment(self, data):
        # Handle comments (no output required)
        pass

    def handle_startendtag(self, tag, attrs):
        # Handle start and end tags (self-closing)
        print("Empty :", tag)
        for (a, v) in attrs:
            # Print attributes of the self-closing tag
            print("->", a, ">", v)

# Initialize an empty string to store the input HTML content
s = ""           

# Read input lines and concatenate them into the string
for _ in range(int(input())):
    s += input() 

# Create an instance of the custom parser
parser = myhtmlparser() 

# Feed the concatenated HTML content to the parser
parser.feed(s)