# Create a class Circle with an attribute radius. Create two objects of circle c1 and c2.
# Add the radius of the circles and print the result.
# Do the above task using a method and then a magic method.
# Compare the size of the circle and print the result using magic method.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def add_radius(self, obj2):
        return self.radius + obj2.radius

    def __add__(self, other):
        return self.radius + other.radius

c1 = Circle(5)
c2 = Circle(7)
result = c1.radius + c2.radius
print(result)

