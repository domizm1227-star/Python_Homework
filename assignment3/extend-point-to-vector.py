# Task 5: Extending a Class
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2
        )


class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )


# Test Point
point1 = Point(3, 4)
point2 = Point(3, 4)
point3 = Point(6, 8)

print("Point 1:", point1)
print("Point 2:", point2)

# Test equality
print("point1 == point2:", point1 == point2)
print("point1 == point3:", point1 == point3)

# Test distance
print("Distance from point1 to point3:", point1.distance(point3))


# Test Vector
vector1 = Vector(2, 3)
vector2 = Vector(4, 5)

print("Vector 1:", vector1)
print("Vector 2:", vector2)

# Test vector addition
vector3 = vector1 + vector2

print("Vector 1 + Vector 2:", vector3)