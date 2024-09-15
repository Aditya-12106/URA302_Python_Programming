import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

radius = float(input("Enter the radius of the circle: "))

circle = Circle(radius)

print(f"Circle with radius {circle.radius}:")
print(f"Area: {circle.area():.2f}")
print(f"Perimeter: {circle.perimeter():.2f}")