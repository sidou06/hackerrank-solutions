from html.parser import HTMLParser

# Define custom HTMLParser class inheriting from HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        # Check if the comment is multi-line or single-line
        if "\n" in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        # Print the content of the comment
        print(data)

    def handle_data(self, data):
        # Handle data (excluding newlines)
        if data != "\n":
            print(">>> Data")
            print(data)

# Initialize an empty string to store the input HTML content
html = ""       

# Read input lines and concatenate them into the string
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
# Create an instance of the custom parser
parser = MyHTMLParser()

# Feed the concatenated HTML content to the parser
parser.feed(html)

# Close the parser after processing
parser.close()