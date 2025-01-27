from functools import reduce
def product(fracs):
    # Calculate the product of fractions in the list fracs
    t = reduce(lambda x, y: x * y, fracs)  # Use reduce to multiply all fractions
    return t.numerator, t.denominator  # Return the numerator and denominator of the result