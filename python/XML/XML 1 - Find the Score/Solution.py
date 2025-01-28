def get_attr_number(node):
    s = len(node.attrib)  # Count the attributes of the current node
    for child in node:  # Recursively process each child node
        s += get_attr_number(child)
    return s  # Return the total attribute count