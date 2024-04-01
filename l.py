class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def get_area(self):
        pass

    def set_radius(self, radius):
        pass

class Rectangle(Shape):
    def get_area(self):
        pass

    def set_width(self, width):
        pass

    def set_height(self, height):
        pass

class Triangle(Shape):
    def get_area(self):
        pass

# Handling differences without violating LSP

# 1. Circle and Rectangle have set_width() and set_height(), while Triangle doesn't.
# Solution: Use optional parameters or provide default values for set_width() and set_height().

# 2. get_area() implementation varies.
# Solution: Ensure consistent parameter naming and calculation logic across all shapes.

# 3. Adding a new Polygon shape.
# Solution: Extend the Shape class for the new Polygon shape.

# Usage
circle = Circle()
rectangle = Rectangle()
triangle = Triangle()
