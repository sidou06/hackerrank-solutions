class Points(object):
    # Initialize a point in 3D space with x, y, z coordinates
    def __init__(self, x, y, z):
        self.x = x 
        self.y = y
        self.z = z 

    # Subtract two points in 3D space
    def __sub__(self, no):
        x = self.x - no.x 
        y = self.y - no.y 
        z = self.z - no.z 
        return Points(x, y, z) 

    # Compute the dot product of two points (vectors)
    def dot(self, no):
        x1, y1, z1 = self.x, self.y, self.z 
        x2, y2, z2 = no.x, no.y, no.z 
        return x1 * x2 + y1 * y2 + z1 * z2 

    # Compute the cross product of two points (vectors)
    def cross(self, no):
        x1, y1, z1 = self.x, self.y, self.z 
        x2, y2, z2 = no.x, no.y, no.z 
        x = y1 * z2 - y2 * z1 
        y = x1 * z2 - x2 * z1 
        z = x1 * y2 - x2 * y1 
        return Points(x, y, z) 

    # Compute the magnitude (absolute value) of a vector
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)