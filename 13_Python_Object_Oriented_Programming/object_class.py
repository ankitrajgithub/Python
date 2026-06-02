# Object = A "bundle" of related attributes (variables) and methods (functions).
# Ex. phone, cup, book
# You need a "class" to create many objects.

# Class = (blueprint) used to design the structure and layout of an object

from car import Car

car1=Car("Hyundai",2021,"Red",False)
car2=Car("Corvette","2025","Blue",True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

car1.drive()
car2.drive()

car1.stop()
car2.stop()

car1.describe()
car2.describe()