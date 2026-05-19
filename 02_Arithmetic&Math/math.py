import math

x=3.14
y=4
z=5

#result=round(x)
#result=abs(y)
#result=pow(z,3)
#result=max(x,y,z)
#result=min(x,y,z)

print(math.pi)
print(math.e)

#result=math.sqrt(y)
#result=math.ceil(x)
#result=math.floor(x)

#print(result)

#Exercise 1 Circle Circumference Calculation
radius=float(input("Enter the radius of the circle : "))
circumference=2*math.pi*radius

print(f"The circumference of the Circle is {round(circumference,2)} cm")

#Exercise 2 Circle Area Calculation
area=math.pi*pow(radius,2)

print(f"The area of the Circle is {round(area,2)} cm²")

#Exercise 3 Hypotenuse of a right-angled triangle
a=float(input("Enter side A : "))
b=float(input("Enter side B : "))

c=math.sqrt(pow(a,2)+pow(b,2))

print(f"Side C : {c}")