# Polymorphism = Greek word that means to "have many forms or faces".
#                Poly = Many
#                Morphe = Form

# TWO WAYS TO ACHIEVE POLYMORPHISM
# 1. Inheritance = An object could be treated of the same type as a parent class
# 2. "Duck typing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of Circle : {3.14*self.radius*self.radius} cm^2.")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"Area of Square : {self.side*self.side} cm^2.")

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print(f"Area of Triangle : {self.base*self.height/2} cm^2.")

class Pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping=topping

shapes=[Circle(4),Square(5),Triangle(6,7),Pizza("Jalapeno",10)]

for shape in shapes:
    shape.area()