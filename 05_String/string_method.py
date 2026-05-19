name=input("Enter your full name : ")
phone_number=input("Enter your phone number : ")

#result=len(name)
#result=name.find(" ")
#result=name.find("A")
#result=name.rfind("a")
#result=name.find("q")
#result=name.isdigit()
#result=name.isalpha()
#result=name.isalnum()
result=phone_number.count("-")
phone_number=phone_number.replace("-"," ")

print(phone_number)

print(result)

#name=name.capitalize()
#name=name.upper()
#name=name.lower()

print(name)

print(help(str))

#Exercise 1 Validate user input exercise
#1. Username is no more than 12 characters
#2. Username must not contain spaces
#3. Username must not contain digits

username=input("Enter your username : ")

if len(username)>12:
    print("Your username is too long")
elif not username.find(" ")==-1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")