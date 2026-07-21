# Task 5: Extending a Class
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        # Checks to see if this point has same coordinates as another
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __str__(self):
        # Will determine how the Point prints
        return f"Point(x={self.x}, y={self.y})"
    
    def distance(self, other):
        # Calculates the Euclidean distance
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

# Create a subclass Vector
class Vector(Point):
    def __str__(self):
#Overriding Point's string representation
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
    # Overloads addition operatpor to return a new vector
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
# Demonstration Results
if __name__ == "__main__":
    print("___ Testing Point Class ---")
    p1 = Point(3, 4)
    p2 = Point(3, 4)
    p3 = Point(0,0)
    
    print(f"p1 representation: {p1}")
    print(f"Is p1 equal to p2? {p1 == p2}")
    print(f"Is p1 equal to p3?{p1 == p3}")
    print(f"Distance from p1 to p3: {p1.distance(p3)}")
    
    print("\n--- Testing Vector Class ---")
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    
    print(f"v1 respresentation: {v1}")
    
    # Testing operator overloading
    v3 = v1 + v2
    print(f"Result of v1 + v2: {v3}")