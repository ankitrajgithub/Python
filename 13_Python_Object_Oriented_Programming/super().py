# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods.
class Shape:
    def __init__(self, color,is_filled):
        self.color=color
        self.is_filled=is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}.")

class Circle(Shape):
    def __init__(self, color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius

    def describe(self):
        print(f"It is a circle with an area of {3.14*self.radius*self.radius} cm^2.")
        super().describe()

class Square(Shape):
    def __init__(self, color,is_filled,width):
        super().__init__(color,is_filled)
        self.width=width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.width*self.width} cm^2.")

class Triangle(Shape):
    def __init__(self, color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width=width
        self.height=height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {self.height*self.width/2} cm^2.")

square=Square("Green",True,5)
print(f"Square Width : {square.width}")
print(f"Square Color : {square.color}")
square.describe()

circle=Circle("Red",False,5)
print(f"Circle Radius : {circle.radius}")
print(f"Circle Color : {circle.color}")
circle.describe()

triangle=Triangle("Blue",True,5,10)
print(f"Triangle Width : {triangle.width}")
print(f"Triangle Height : {triangle.height}")
print(f"Triangle Color : {triangle.color}")
triangle.describe()