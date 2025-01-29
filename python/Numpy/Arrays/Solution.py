import numpy
def arrays(arr):
    # Convert list to numpy array with float type
    r = numpy.array(arr, float)
    # Reverse the array
    r = numpy.flip(r)
    return r