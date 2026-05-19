#Variable - A container for a value (string, boolean, integer, float)

#Strings
first_name="Ankit"
print(first_name)

last_name="Raj"
print(last_name)

#f String
print(f"Hello {first_name} {last_name}")

#Integers
age=22
print(age)
print(f"You are {age} years old")

#Floats
price=10.99
print(f"The price is {price}")

#Booleans
is_student=True
print(f"Are you a student: {is_student}")

#If-Else Loop
if is_student:
    print("You are a student")
else:
    print("You are not a student")

for_sale=False

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

#Typecasting - The process of converting a variable from one data type to another. str(), int(), float(), bool()

name="Ankit Raj"
age=22
gpa=3.2
is_student=True

gpa=int(gpa)
print(type(gpa))
print(gpa)

age=float(age)
print(type(age))
print(age)

age=str(age)
age=age+"1"
print(type(age))
print(age)

name=bool(name)
print(type(name))
print(name)
