# while loop = execute some code WHILE some condition remains true

name=input("Enter your name : ")

while name=="":
    print("Your name is empty")
    name=input("Enter your name : ")

print(f"Hello {name}!")

age=int(input("Enter your age : "))
while age<0:
    print("Your age can't be less than zero")
    age=int(input("Enter your age : "))

print(f"Your age is {age}")

food=input("Enter a food you like (q to quit) : ")

while not food=="q":
    print("You like :",food)
    food=input("Enter another food you like (q to quit) : ")

num=int(input("Enter a number between 1-10 : "))

while num<1 or num>10:
    print("Your number must be between 1-10")
    num=int(input("Enter a number between 1-10 : "))

print(f"Your number is {num}")

#Python compound interest calculator


principal=float(input("Enter a principal : "))

while principal<=0:
    print("Your principal must be greater than zero")
    principal=float(input("Enter a principal : "))

rate=float(input("Enter a rate : "))

while rate<=0:
    print("Your rate must be greater than zero")
    rate=float(input("Enter a rate : "))

time=0

while True:
    time = int(input("Enter a time : "))
    if time<=0:
        print("Your time must be greater than zero")
    else:
        break

years=time

total=principal*pow((1+rate/100),time)

while years>0:
    principal=principal+(principal*rate/100)
    years-=1

print(f"Your principal is {principal} in {time} years at {rate}% interest.")
print(f"Your principal is {total:.2f} in {time} years at {rate}% interest.")