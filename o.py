from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def get_area(self):
        pass

class Square(Shape):
    def get_area(self):
        pass

class Rectangle(Shape):
    def get_area(self):
        pass

# Usage
circle = Circle()
square = Square()
rectangle = Rectangle()
