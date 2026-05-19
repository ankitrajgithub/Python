#if - Do some code only IF some condition is True
#     Else do something else

age=int(input("Enter your age : "))

#if Statement
if age>=18:
    print("You are signed up!")

#else-if Statement
if age>=18:
    print("You are eligible for credit card!")
else:
    print("You are not eligible for credit card!")

#if-elif-else Statement
if age>18:
    print("You are greater than 18 years")
elif age==18:
    print("You are 18 years old")
else:
    print("You are less than 18 years")

response=input("Would you like some food?(Y/N) : ")
if response=="Y":
    print("Have some food!")
elif response=="N":
    print("No food for you!")
else:
    print("Invalid input!")

name=input("Enter your name : ")
if name=="":
    print("You haven't typed in your name")
else:
    print(f"Hello {name}!")

for_sale=True
if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

#Python Calculator
operator=input("Enter an operator (+ - * /) : ")

num1=float(input("Enter first number : "))
num2=float(input("Enter second number : "))

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else:
    print("Invalid operator")

#Python weight converter

weight=float(input("Enter your weight : "))
unit=input("Kilograms or Pounds?(K/L) : ")

if unit=="K":
    weight=weight*2.205
    unit="Lb"
    print(f"Your weight is : {round(weight, 2)} {unit}.")
elif unit=="L":
    weight=weight/2.205
    unit="Kg"
    print(f"Your weight is : {round(weight, 2)} {unit}.")
else:
    print("Invalid unit")

#Python temperature conversion
unit=input("Is this temperature in Celsius or Fahrenheit?(C/F) : ")
temp=float(input("Enter your temperature : "))

if unit=="C":
    temp=round((temp*9)/5+32,2)
    print(f"Your temperature is : {temp} °F.")
elif unit=="F":
    temp=round((temp-32)*5/9,2)
    print(f"Your temperature is : {temp} °C.")
else:
    print("Invalid unit")

