# module =  File containing code you want to include in your program
#           Use 'import' to include a module (built-in or your own)
#           Useful to break up a large program reusable separate files

#import math
#import math as m
from math import pi,e

print(pi)
print(e)

import external_module

area=external_module.area(3)
print(area)

square=external_module.square(3)
print(square)

cube=external_module.cube(3)
print(cube)

circumference=external_module.circumference(3)
print(circumference)

#print(help("modules"))
#print(help("math"))
#print(type(help("modules")))