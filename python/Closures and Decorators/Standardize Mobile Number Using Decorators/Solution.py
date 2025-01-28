def wrapper(f):
    def fun(l):
        # Format each phone number in the list
        for i in range(len(l)):
            l[i] = "+91 " + l[i][-10:-5] + " " + l[i][-5:]
        # Call the original function with the formatted list
        return f(l) 
    return fun