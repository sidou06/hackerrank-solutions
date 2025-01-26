class Complex(object):
    # Initialize the complex number with real and imaginary parts
    def __init__(self, real, imaginary):
        self.real = real 
        self.imaginary = imaginary 

    # Add two complex numbers
    def __add__(self, no):
        x = self.real + no.real 
        y = self.imaginary + no.imaginary 
        return Complex(x, y)

    # Subtract one complex number from another
    def __sub__(self, no):
        x = self.real - no.real 
        y = self.imaginary - no.imaginary 
        return Complex(x, y)

    # Multiply two complex numbers
    def __mul__(self, no):
        x1 = self.real  
        y1 = self.imaginary 
        x2 = no.real 
        y2 = no.imaginary 
        x = x1 * x2 - y1 * y2 
        y = x1 * y2 + y1 * x2 
        return Complex(x, y) 

    # Divide one complex number by another
    def __truediv__(self, no):
        x1 = self.real  
        y1 = self.imaginary
        x2 = no.real 
        y2 = no.imaginary 
        # Multiply numerator by the conjugate of the denominator
        n = self * Complex(x2, -y2)
        # Calculate denominator as the square of the modulus
        d = x2 ** 2 + y2 ** 2
        n1 = n.real / d 
        n2 = n.imaginary / d 
        return Complex(n1, n2)

    # Calculate the modulus of the complex number
    def mod(self):
        x = self.real   
        y = self.imaginary    
        m = (x ** 2 + y ** 2) ** 0.5
        return Complex(m, 0)

    # String representation of the complex number
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result